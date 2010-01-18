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
import mapnik

# append the DMLib and local directories to PYTHONPATH
local_dir = os.path.dirname(__file__)
sys.path.append(local_dir)
from olMapControl import olMapControl
from MapnikResponder import MapnikResponder
from MapnikResponder import PreviewThread

class MapResponder2(MapnikResponder):
  """the default map responder, which outputs the result from the executor"""
  def __init__(self, id, dialogue, kb = None, planGraph = None, executor = None):
    MapnikResponder.__init__(self, id, dialogue, kb, planGraph, executor)
    
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
  
  def __generateMapFile(self):
    """docstring for __generateMapFile"""
    # load the base map template
    mapnik_map_file = os.path.join(os.path.dirname(__file__), self.config["mapnik_template_dir"], "basemap.xml")
    # do some modification to the map file
    m = mapnik.Map(256, 256)
    mapnik.load_map(m, str(mapnik_map_file))
    
    lyr = mapnik.Layer('world_merc', m.srs)
    layer_file = os.path.join(os.path.dirname(__file__), self.config["data_dir"], "world_merc")
    lyr.datasource = mapnik.Shapefile(file=str(layer_file))
    lyr.styles.append('population')
    lyr.styles.append('countries_label')
    m.layers.append(lyr)
    # copy the map file to the output directory
    
    output_dir = os.path.join(self.output_base_dir, self.timestamp)
    if not os.path.exists(output_dir):
      os.makedirs(output_dir)
    output_mapfile = os.path.join(output_dir, 'map.xml')
    mapnik.save_map(m, str(output_mapfile))
  
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
    # make decisions on the map scale, map layers
    #mockup
    self.bbox = (-70.0, 0.0, 70.0, 45.0)
    #self.bbox = (-77.97, 40.7, -77.75, 40.87)
    # 0. get the current timestamp
    self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # generate the xml map file
    # 1. load the base map from the template and output it
    self.__generateMapFile()
    # 2. generate the static preview pictures
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