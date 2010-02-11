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
        
def _cartesian_product(L,*lists):
    if not lists:
        for x in L:
            yield (x,)
    else:
        for x in L:
            for y in _cartesian_product(lists[0],*lists[1:]):
                yield (x,)+y
                                    
class MapListResponder():
    """show a list of possible map reponses based on the reasoning rules"""
    def __init__(self, dialogue, params=None):
        self.channels = []
        self.dialogue = dialogue
        self.params = params
        self.kb = self.dialogue.kb
        self.planGraph = self.dialogue.planGraph
        self.executor = self.dialogue.executor
        self.type = "maplist"    # the type of generated response content (e.g. text message, map, etc...)
        
        # set up map file
        f = open(os.path.join(os.path.dirname(__file__), 'map.yaml'))
        self.config = yaml.load(f)
        f.close()
        self.output_base_dir = os.path.join(self.config["output_base_dir"], self.dialogue.id)
        if not os.path.exists(self.output_base_dir):
            os.makedirs(self.output_base_dir)
        self.output_base_url = self.config["map_server"] + "/" + self.dialogue.id
        self.timestamp = ""
        self.ol_template_dir = os.path.join(os.path.dirname(__file__), self.config["ol_template_dir"])
        self.olMapCtrl = olMapControl(self.ol_template_dir)
        # set up reasoning engine
            
        if self.params and self.params.get("kbase", ""):
            self.engine = knowledge_engine.engine(self.params["kbase"])
        
    def getResponseContent(self, responseId):
        """return the generated content of this responder"""
        for channel in self.channels:
            if channel["id"] == responseId:
                self.olMapCtrl.setMapExtent(channel["bbox"][0], channel["bbox"][1], channel["bbox"][2], channel["bbox"][3])
                layerInfo = {}
                layerInfo["name"] = "mapnik"
                layerInfo["title"] = "mapnik"
                layerInfo["url"] = channel["output_base_url"] + "/" + self.timestamp + "/tiles/${z}/${x}/${y}.png"
                self.olMapCtrl.addMapLayer("XYZ", layerInfo)
                response = {}
                response["type"] = channel["type"]
                response["content"] = self.olMapCtrl.saveXML()
                return response
        response = {}
        response["status"] = "error"
        response["message"] = "cannot find the response Id"
        return response
    
    def getResponseChannels(self):
        """docstring for getResponseChannels"""
        channels = []
        for channel in self.channels:
            resp = {}
            resp["id"] = channel["id"]
            resp["type"] = channel["type"]
            resp["name"] = channel["id"] 
            channels.append(resp)
        return channels
    
    def getCurrentResponses(self):
        """docstring for getCurrentResponses"""
        responses = []
        for channel in self.channels:
            response = {}
            response["type"] = channel["type"]
            response["id"] = channel["id"]
            response["preview"] = channel["preview"]
            response["explanation"] = channel["explanation"]
            responses.append(response)
        return responses    
                 
    def __assertPlanGraphFacts(self):
        """traverse the plangraph to generate the specific facts"""
        if self.planGraph and self.planGraph.root:
            self.__assertPlanNodeFacts(self.planGraph.root)
        # is_focus
        for focus in self.planGraph.focus:
            if focus.actionType == "ID_PARA" and focus.refPhrase:
                actionName = focus.actionName + '_' + '_'.join(focus.refPhrase.split())
            else:
                actionName = focus.actionName
            self.engine.assert_('plangraph', 'is_focus', (actionName,))
            
    def __assertPlanNodeFacts(self, plan):
        if plan.actionType == "ID_PARA" and plan.refPhrase:
            actionName = plan.actionName + '_' + '_'.join(plan.refPhrase.split())
        else:
            actionName = plan.actionName
        # status_of
        self.engine.assert_('plangraph', 'status_of', (exec_status[plan.mentalState.execStatus], actionName))
        # type_of
        self.engine.assert_('plangraph', 'type_of', ('action', actionName))
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
        
        # generated_value_of & type_of
        for value in plan.generatedValues:
            self.engine.assert_('plangraph', 'generated_value_of', (value, actionName))
            if self.kb:
                content_type = self.kb.getGeoContentType(value)
                if content_type:
                    self.engine.assert_('geocontent', 'type_of', (content_type, value))
                    
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
        # type_of
        self.engine.assert_('plangraph', 'type_of', ('param', param.name))
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
        self.engine.get_kb('geocontent', fact_base.fact_base)
        self.engine.get_kb('maprole', fact_base.fact_base)
        self.engine.get_kb('maptask', fact_base.fact_base)
        self.engine.get_kb('mapstra', fact_base.fact_base)
        self.engine.activate('testcase2')
        self.engine.get_kb('maprole').dump_specific_facts()

                    
    def __generateResponseChannels(self):
        self.tasks = []
        stras_list = []
        task_base = self.engine.get_kb("maptask")
        stra_base = self.engine.get_kb("mapstra")
        for task_name in task_base.entity_lists.iterkeys():
            task = {}
            task["name"] = task_name
            task["entities"] = []
            for entity in task_base.entity_lists[task_name].case_specific_facts:
                task["entities"].append(entity)
            task["stras"] = {}
            stras = []
            for stra_name in stra_base.entity_lists.iterkeys():
                if stra_name == 'fulfill':
                    fulfill_stra = stra_base.entity_lists[stra_name]
                    for entity in fulfill_stra.case_specific_facts:
                        if entity[1] == task_name and (not entity[0] in stras):
                            stras.append(entity[0])
                            task["stras"][entity[0]] = entity[2]
            self.tasks.append(task)
            if stras:
                stras_list.append(stras)
        self.channels = []
        print stras_list
        for stra in _cartesian_product(*stras_list):
            channel = {}
            channel["id"] = str(len(self.channels))
            channel["type"] = "map"
            channel["stra"] = stra
            channel["bbox"] = None
            channel["center"] = None
            channel["mapContents"] = {}
            channel["preview"] = ""
            channel["explanation"] = ""
            channel["output_base_dir"] = os.path.join(self.output_base_dir, channel["id"])
            if not os.path.exists(channel["output_base_dir"]):
                os.makedirs(channel["output_base_dir"])
            channel["output_base_url"] =  self.output_base_url + "/" + channel["id"]
            self.channels.append(channel)
    
    def __generateResponses(self):
        for channel in self.channels:
            self.__generateResponse(channel)
    
    def __generateResponse(self, channel):
        # make decisions on the map scale, map contents 
        self.__getMapView(channel)
        # generate the explanation
        self.__generateExplanation(channel)
        # generate the xml map file
        self.__generateMapFile(channel)
        # generate the static preview pictures
        self.__generatePreview(channel)

        
    def __getMapView(self, channel):
        # set default value
        channel["bbox"] = [-8545941.648454214, 4883905.226215085, -8536034.213773614, 4892847.935304075]
        channel["center"] = None
        channel["mapContents"] = {}
        
        fbase = self.engine.get_kb("mapstra")
        visible_features = []
        visible_in_ctx_features = []
        #highlight_features = []
        center_features = []
        for fl_name in fbase.entity_lists.iterkeys():
            if fl_name in channel["stra"]: 
                fact_list = fbase.entity_lists[fl_name]
                for fact in fact_list.case_specific_facts:
                    if fact[0] == 'scale_level':
                        self.__setBbox(channel, fact[1])
                    elif fact[0] == 'center':
                        center_features.append(fact[1])
                        #self.__setCenter(channel, fact[1])
                    elif fact[0] == 'layer':
                        self.__addMapContent(channel, fact[1])
                    elif fact[0] == 'visible':
                        visible_features.append(fact[1])
                    elif fact[0] == 'visible_in_context':
                        visible_in_ctx_features.append(fact[1])
                    elif fact[0] == 'highlight':
                        #highlight_features.append(fact[1])
                        self.__addMapStyle(channel, fact[1], 'highlight')
        if visible_features:
            self.__extendBbox(channel, self.kb.getBbox(visible_features))
        if visible_in_ctx_features:
            bbox = self.kb.getBbox(visible_in_ctx_features)
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            bbox[0] = bbox[0] - 0.5 * width
            bbox[1] = bbox[1] - 0.5 * height
            bbox[2] = bbox[2] + 0.5 * width
            bbox[3] = bbox[3] + 0.5 * height
            self.__extendBbox(channel, bbox)
        if center_features:
            bbox = self.kb.getBbox(center_features)
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            channel["center"] = (bbox[0] + 0.5 * width, bbox[1] + 0.5 * height)
            
        if channel["bbox"] and channel["center"]:
            width = channel["bbox"][2] - channel["bbox"][0]
            height = channel["bbox"][3] - channel["bbox"][1]
            channel["bbox"][0] = channel["center"][0] - 0.5 * width
            channel["bbox"][2] = channel["center"][0] + 0.5 * width
            channel["bbox"][1] = channel["center"][1] - 0.5 * height
            channel["bbox"][3] = channel["center"][1] + 0.5 * height
            
            
    def __addMapStyle(self, channel, value, style):
        content = channel["mapContents"].get(value, {})
        if not content:
            content = self.__addMapContent(channel, value)
        if not (style in content["styles"]):
            content["styles"].append(style)
        
    def __addMapContent(self, channel, value):
        content = channel["mapContents"].get(value, {})
        if not content:
            new_content = {}
            new_content["name"] = value
            new_content["styles"] = []
            channel["mapContents"][value] = new_content
            return new_content
        
    def __setCenter(self, channel, value):
        if self.kb:
            center = self.kb.getGeoContentCenter(value)
            if center:
                channel["center"] = center
    
    def __extendBbox(self, channel, bbox):
        if bbox:
            if not channel["bbox"]:
                channel["bbox"] = bbox
            else:
                channel["bbox"][0] = min(channel["bbox"][0], bbox[0])
                channel["bbox"][1] = min(channel["bbox"][1], bbox[1])
                channel["bbox"][2] = max(channel["bbox"][2], bbox[2])
                channel["bbox"][3] = max(channel["bbox"][3], bbox[3])
                                        
    def __setBbox(self, channel, scale_level):
        # TODO add to knowledge base
        bbox = []
        if scale_level == 'state':
            bbox = [-8854449.813570915, 4830153.383535952, -8476288.5977869, 5159633.330083089]        
        elif scale_level == 'local':
            bbox = [-8545941.648454214, 4883905.226215085, -8536034.213773614, 4892847.935304075]
        elif scale_level == 'county':
            bbox = [-8554791.214013807, 4873928.498204929, -8527832.52765044, 4899503.996841681]
        elif scale_level == 'region':
            bbox = [-8574408.602598343, 4855651.740543485, -8508086.231095564, 4918399.766340519]
        elif scale_level == 'country':
            bbox = [-13852053.638602437, 933101.2722854596, -4975574.699678951, 7526228.245446581]
        self.__extendBbox(channel, bbox)    
    
    def __generateExplanation(self, channel):
        explanation = "<ul class='explanation'>"
        for task in self.tasks:
            if task["entities"]:
                task_desp = "<li class='map_task'>"
                task_desp += "<dl class='task_details'>"
                task_desp += "<dt><span class='task_name'>" + task["name"] + ": </span>"
                task_list = []
                for entity in task["entities"]:
                    task_list.append(entity[0])
                task_desp += "<span class='task_list'>" + ', '.join(task_list) + "</span></dt>"
                task_desp += "<dd>" + task["entities"][0][1] + "<br/>"
                for task_stra in channel["stra"]:
                    stra_exp = task["stras"].get(task_stra, "")
                    if stra_exp:
                        task_desp += "<p><b>Strategy: </b>" + stra_exp + "</p>"
                task_desp += "</dd></dl></li>"
                explanation += task_desp
        explanation += "</ul>"
        channel["explanation"] = explanation
    
    def __generateMapFile(self, channel):
        # load the base map template
        mapnik_map_file = os.path.join(os.path.dirname(__file__), self.config["mapnik_template_dir"], "osm_basemap.xml")
        base_map_doc = minidom.parse(mapnik_map_file)
        base_map_dom = base_map_doc.documentElement
        mapnik_template_dir = os.path.join(os.path.dirname(__file__), self.config["mapnik_template_dir"])
        layer_loader = TemplateLoader(os.path.join(mapnik_template_dir, 'layers'), auto_reload=False)
        style_loader = TemplateLoader(os.path.join(mapnik_template_dir, 'styles'), auto_reload=False)
        style_string = style_loader.load('feature.xml').generate(mapnik_template_dir=mapnik_template_dir).render()
        style_doms = minidom.parseString(style_string).getElementsByTagName("Style")
        for style_dom in style_doms:
            base_map_dom.appendChild(style_dom)
        features = {}
        for content in channel["mapContents"].values():
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
                    features[name] = styles
        featureInfo = {}
        featureInfo['host'] = self.executor.datasource["host"]
        featureInfo['port'] = self.executor.datasource["port"]
        featureInfo['dbname'] = self.executor.datasource["dbname"]
        featureInfo['user'] = self.executor.datasource["user"]
        featureInfo['password'] = self.executor.datasource["password"]
        feature_names = self.kb.getOrderedFeatures(features.keys())
        for name in feature_names:
            styles = features[name]
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

        output_dir = os.path.join(channel["output_base_dir"], self.timestamp)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_mapfile = os.path.join(output_dir, 'map.xml')
        f = open(output_mapfile, 'w')        
        base_map_doc.writexml(f)
        f.close()
                    
    def __generateMapFile_old(self, channel):
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
                                
        for content in channel["mapContents"].values():
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
        output_dir = os.path.join(channel["output_base_dir"], self.timestamp)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_mapfile = os.path.join(output_dir, 'map.xml')
        f = open(output_mapfile, 'w')        
        base_map_doc.writexml(f)
        f.close()
    
    def __generatePreview(self, channel):
        """docstring for __generatePreview"""
        request = {}
        request["width"] = int(self.config["preview"]["width"])
        request["height"] = int(self.config["preview"]["height"])
        request["minx"] = channel["bbox"][0]
        request["miny"] = channel["bbox"][1]
        request["maxx"] = channel["bbox"][2]
        request["maxy"] = channel["bbox"][3]
        url = channel["output_base_url"] + "/" + self.timestamp + "/static." + self.config["preview"]["format"]
        PreviewThread(url, request).start()
        channel["preview"] = url

        
    def generate(self):
        """generate the response"""
        # do the reasoning
        self.__reason()
        # generate the response channels
        self.__generateResponseChannels()
        # get the current timestamp
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # generate responses
        self.__generateResponses() 

        
def main():
       pass

if __name__ == '__main__':
    main()