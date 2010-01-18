#!/usr/bin/env python
# encoding: utf-8
"""
The class definition for MapResponder

Created by Bo Yu on 2010-01-02.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os
import datetime
import yaml
import urllib, urllib2
import json
import xml.dom.minidom as minidom

# append the DMLib and local directories to PYTHONPATH
local_dir = os.path.dirname(__file__)
sys.path.append(local_dir)
DMLib_dir = local_dir + "/../../DMLib"
sys.path.append(DMLib_dir) 
from MentalState import *
from PlanGraph import *

from olMapControl import olMapControl

from pyke import knowledge_engine
from pyke import fact_base

from genshi.template import TemplateLoader

import threading

class PreviewThread(threading.Thread):
        """create a thread to generate the preview"""
        def __init__(self, url, data):
                super(PreviewThread, self).__init__()
                self.url = url
                self.data = data
        def run (self):
                f = urllib2.urlopen(self.url, json.dumps(self.data))
                f.close()
        
                
class MapnikResponder():
    """the default map responder, which outputs the result from the executor"""
    def __init__(self, id, dialogue, params=None):
        self.id = id
        self.dialogue = dialogue
        self.params = params
        self.kb = self.dialogue.kb
        self.planGraph = self.dialogue.planGraph
        self.executor = self.dialogue.executor
        self.type = "map"    # the type of generated response content (e.g. text message, map, etc...)
        self.bbox = None
        self.center = None
        self.mapContents = {}
        # set up map file
        f = open(os.path.join(os.path.dirname(__file__), 'map.yaml'))
        self.config = yaml.load(f)
        f.close()
        self.output_base_dir = os.path.join(self.config["output_base_dir"], self.dialogue.id, self.id)
        if not os.path.exists(self.output_base_dir):
            os.makedirs(self.output_base_dir)
        self.output_base_url = self.config["map_server"] + "/" + self.dialogue.id + "/" + self.id
        self.timestamp = ""
        self.ol_template_dir = os.path.join(os.path.dirname(__file__), self.config["ol_template_dir"])
        self.olMapCtrl = olMapControl(self.ol_template_dir)
        # set up reasoning engine
            
        if self.params and self.params.get("kbase", ""):
            self.engine = knowledge_engine.engine(self.params["kbase"])
            self.testcase = self.params.get("testcase", -1)
        
        
    def getResponseContent(self):
        """return the generated content of this responder"""
        
        self.olMapCtrl.setMapExtent(self.bbox[0], self.bbox[1], self.bbox[2], self.bbox[3])
        layerInfo = {}
        layerInfo["name"] = "mapnik"
        layerInfo["title"] = "mapnik"
        layerInfo["url"] = self.output_base_url + "/" + self.timestamp + "/tiles/${z}/${x}/${y}.png"
        self.olMapCtrl.addMapLayer("XYZ", layerInfo)
        response = {}
        response["type"] = self.type
        response["content"] = self.olMapCtrl.saveXML()
        return response
    
    def __assertPlanGraphFacts(self):
        """traverse the plangraph to generate the specific facts"""
        if self.planGraph and self.planGraph.root:
            self.__assertPlanNodeFacts(self.planGraph.root)
            
    def __assertPlanNodeFacts(self, plan):
        if plan.actionType == "ID_PARA" and plan.refPhrase:
            actionName = plan.actionName + '_' + '_'.join(plan.refPhrase.split())
        else:
            actionName = plan.actionName
        # status_of
        self.engine.assert_('plangraph', 'status_of', (exec_status[plan.mentalState.execStatus], actionName))
        # action_type_of
        self.engine.assert_('plangraph', 'action_type_of', (plan.actionType, actionName))
        # action_complexity_of
        self.engine.assert_('plangraph', 'action_complexity_of', (plan.complexity, actionName))    
        
        # subaction_of
        if plan.parent:
            if plan.parent.__class__.__name__ == 'PlanNode': #isinstance(plan.parent, PlanNode):
                if plan.parent.actionType == "ID_PARA" and plan.parent.refPhrase:
                    parent_name = plan.parent.actionName + '_' + '_'.join(plan.parent.refPhrase.split())
                else:
                    parent_name = plan.parent.actionName
            elif plan.parent.__class__.__name__ == 'ParamNode': #isinstance(plan.parent, ParamNode):
                parent_name = plan.parent.name
            self.engine.assert_('plangraph', 'subaction_of', (actionName, parent_name))
        
        # generated_value_of
        for value in plan.generatedValues:
            self.engine.assert_('plangraph', 'generated_value_of', (value, actionName))
        # int_status & exec_status
        for agent in plan.agents:
            self.engine.assert_('plangraph', 'int_status', (str(agent.id), actionName, int_status[agent.mentalState.intention]))
            self.engine.assert_('plangraph', 'exec_status', (str(agent.id), actionName, exec_status[agent.mentalState.execStatus]))
        # context_of & type_of
            
        if self.kb:
            contents = self.kb.getActionContext(plan.actionName)
            for content in contents:
                self.engine.assert_('plangraph', 'context_of', (content, actionName))
                content_type = self.kb.getGeoContentType(content)
                if content_type:
                    self.engine.assert_('geocontent', 'type_of', (content_type, content))
        # parameters
        for param in plan.params:
            self.__assertParamNodeFacts(param)
                
        # subactions
        for subPlan in plan.subPlans:
            self.__assertPlanNodeFacts(subPlan)    
    
    def __assertParamNodeFacts(self, param):
        # param_of
        if param.parent:
            if param.parent.actionType == "ID_PARA" and param.parent.refPhrase:
                parent_name = param.parent.actionName + '_' + '_'.join(param.parent.refPhrase.split())
            else:
                parent_name = param.parent.actionName
            self.engine.assert_('plangraph', 'param_of', (param.name, parent_name))
        # status_of
        self.engine.assert_('plangraph', 'status_of', (param_status[param.status], param.name))
        # param_type_of
        self.engine.assert_('plangraph', 'param_type_of', (param_type[param.type], param.name))    
        # value_of & geocontent.type_of
        for value in param.values:
            if value:
                self.engine.assert_('plangraph', 'value_of', (value, param.name))
                if param.type == param_type_geoType:
                    if self.kb:
                        value_type = self.kb.getGeoContentType(value)
                        if value_type:
                            self.engine.assert_('geocontent', 'type_of', (value_type, value))
        # is_multiple
        if param.multiple:
            self.engine.assert_('plangraph', 'is_multiple', (param.name,))
        # subactions
        for subPlan in param.subPlans:
            self.__assertPlanNodeFacts(subPlan)
            
    def __reason(self):
        self.engine.reset()
        self.__assertPlanGraphFacts()
        if self.testcase > -1:
            self.engine.assert_('test', 'case_number', (self.testcase, ))
            self.engine.get_kb('maprole', fact_base.fact_base)
            self.engine.get_kb('maptask', fact_base.fact_base)
            self.engine.get_kb('mapview', fact_base.fact_base)
            self.engine.activate('testcase')
        
    
    def __getMapView(self):
        self.bbox = None
        self.center = None
        self.mapContents = {}
        fbase = self.engine.get_kb("mapview")
        for fl_name in fbase.entity_lists.iterkeys():
            fact_list = fbase.entity_lists[fl_name]
            if fl_name == 'scale_level':
                for args in fact_list.case_specific_facts:
                    self.__setBbox(args[0])
            elif fl_name == 'center':
                for args in fact_list.case_specific_facts:
                    self.__setCenter(args[0])
            elif fl_name == 'layer':
                for args in fact_list.case_specific_facts:
                    self.__addMapContent(args[0])
            elif fl_name == 'marker':
                for args in fact_list.case_specific_facts:
                    self.__addMapStyle(args[0], 'marker')
            elif fl_name == 'label':
                for args in fact_list.case_specific_facts:
                    self.__addMapStyle(args[0], 'label')
        if self.bbox and self.center:
            width = self.bbox[2] - self.bbox[0]
            height = self.bbox[3] - self.bbox[1]
            self.bbox[0] = self.center[0] - 0.5 * width
            self.bbox[2] = self.center[0] + 0.5 * width
            self.bbox[1] = self.center[1] - 0.5 * height
            self.bbox[3] = self.center[1] + 0.5 * height
            
            
    def __addMapStyle(self, value, style):
        content = self.mapContents.get(value, {})
        if not content:
            content = self.__addMapContent(value)
        if not (style in content["styles"]):
            content["styles"].append(style)
        
    def __addMapContent(self, value):
        content = self.mapContents.get(value, {})
        if not content:
            new_content = {}
            new_content["name"] = value
            new_content["styles"] = []
            self.mapContents[value] = new_content
            return new_content
        
    def __setCenter(self, value):
        if self.kb:
            center = self.kb.getGeoContentCenter(value)
            if center:
                self.center = center
                                    
    def __setBbox(self, scale_level):
        # TODO add to knowledge base
        if scale_level == 'state':
            bbox = [-8854449.813570915, 4830153.383535952, -8476288.5977869, 5159633.330083089]        
        elif scale_level == 'local':
            bbox = [-8542566.21885438, 4883818.023628373, -8538617.716515945, 4887580.225374401]
        elif scale_level == 'county':
            bbox = [-8554791.214013807, 4873928.498204929, -8527832.52765044, 4899503.996841681]
        elif scale_level == 'region':
            bbox = [-8574408.602598343, 4855651.740543485, -8508086.231095564, 4918399.766340519]
        elif scale_level == 'country':
            bbox = [-13852053.638602437, 933101.2722854596, -4975574.699678951, 7526228.245446581]
        if not self.bbox:
            self.bbox = bbox
        else:
            if (self.bbox[2] - self.bbox[0]) * (self.bbox[3] - self.bbox[1]) <  (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]):
                self.bbox = bbox
            
    def __generateMapFile(self):
        """docstring for __generateMapFile"""
        # load the base map template
        mapnik_map_file = os.path.join(os.path.dirname(__file__), self.config["mapnik_template_dir"], "basemap.xml")
        mapInfo = {}
        mapInfo['data_dir'] = os.path.join(os.path.dirname(__file__), self.config["data_dir"])
        mapInfo['mapnik_template_dir'] = os.path.join(os.path.dirname(__file__), self.config["mapnik_template_dir"])
        mapInfo['host'] = self.config["host"]
        mapInfo['port'] = self.config["port"]
        mapInfo['dbname'] = self.config["dbname"]
        mapInfo['user'] = self.config["user"]
        mapInfo['password'] = self.config["password"]
        map_loader = TemplateLoader(mapInfo['mapnik_template_dir'], auto_reload=False)
        base_map_string = map_loader.load('basemap.xml').generate(mapInfo=mapInfo).render()
        base_map_doc = minidom.parseString(base_map_string)
        base_map_dom = base_map_doc.documentElement
        
        layer_loader = TemplateLoader(os.path.join(mapInfo['mapnik_template_dir'], 'layers'), auto_reload=False)
        style_loader = TemplateLoader(os.path.join(mapInfo['mapnik_template_dir'], 'styles'), auto_reload=False)
        style_string = style_loader.load('feature.xml').generate(mapInfo=mapInfo).render()
        
        style_doms = minidom.parseString(style_string).getElementsByTagName("Style")
        for style_dom in style_doms:
            base_map_dom.appendChild(style_dom)
                                
        for content in self.mapContents.values():
            name = content["name"]
            styles = content["styles"]
            if self.kb:
                type = self.kb.getGeoContentType(name)
                if type == "layer":
                    style_string = style_loader.load('%s.xml' % name).generate(mapInfo=mapInfo).render()
                    style_doms = minidom.parseString(style_string).getElementsByTagName("Style")
                    for style_dom in style_doms:
                        base_map_dom.appendChild(style_dom)
                    layer_string = layer_loader.load('%s.xml' % name).generate(mapInfo=mapInfo).render()
                    layer_doms = minidom.parseString(layer_string).getElementsByTagName("Layer")
                    for layer_dom in layer_doms:
                        base_map_dom.appendChild(layer_dom)
                else:
                    featureInfo = {}
                    featureInfo['host'] = self.executor.datasource["host"]
                    featureInfo['port'] = self.executor.datasource["port"]
                    featureInfo['dbname'] = self.executor.datasource["dbname"]
                    featureInfo['user'] = self.executor.datasource["user"]
                    featureInfo['password'] = self.executor.datasource["password"]
                    featureInfo['name'] = name
                    featureInfo['layername'] = '_'.join(name.split())
                    layer_string = layer_loader.load('feature.xml').generate(featureInfo=featureInfo).render()
                    layer_dom = minidom.parseString(layer_string).getElementsByTagName("Layer")[0]
                    style = self.kb.getGeoContentStyle(name)
                    if style:
                        styleNode = base_map_doc.createElement("StyleName")
                        styleNode.appendChild(base_map_doc.createTextNode(style))
                        layer_dom.appendChild(styleNode)
                    for extra_style in styles:
                        if extra_style != style:
                            styleNode = base_map_doc.createElement("StyleName")
                            styleNode.appendChild(base_map_doc.createTextNode(extra_style))
                            layer_dom.appendChild(styleNode)
                    base_map_dom.appendChild(layer_dom)    
        output_dir = os.path.join(self.output_base_dir, self.timestamp)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_mapfile = os.path.join(output_dir, 'map.xml')
        f = open(output_mapfile, 'w')        
        base_map_doc.writexml(f)
        f.close()
    
    def __generatePreview(self):
        """docstring for __generatePreview"""

        request = {}
        request["width"] = int(self.config["preview"]["width"])
        request["height"] = int(self.config["preview"]["height"])
        request["minx"] = self.bbox[0]
        request["miny"] = self.bbox[1]
        request["maxx"] = self.bbox[2]
        request["maxy"] = self.bbox[3]
        url = self.output_base_url + "/" + self.timestamp + "/static." + self.config["preview"]["format"]
        PreviewThread(url, request).start()
        self.preview = url

        
    def generate(self):
        """generate the response"""
        # do the reasoning
        self.__reason()
        # make decisions on the map scale, map contents 
        self.__getMapView()
        # get the current timestamp
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # generate the xml map file
        self.__generateMapFile()
        # generate the static preview pictures
        self.__generatePreview()
        
        
    def getResponse(self):
        """docstring for getResponse"""
        response = {}
        response["type"] = self.type
        response["id"] = self.id
        response["preview"] = self.preview  # the url of the preview map picture
        response["explanation"] = "the explanation of the response"
        return response
        
def main():
       pass

if __name__ == '__main__':
    main()