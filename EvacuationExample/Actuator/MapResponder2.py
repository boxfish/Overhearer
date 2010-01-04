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
import shutil
import yaml
import mapnik

class MapResponder2():
  """the default map responder, which outputs the result from the executor"""
  def __init__(self, id, dialogue, kb = None, planGraph = None, executor = None):
    self.id = id
    self.dialogue = dialogue
    if kb != None:
      self.kb = kb
    else:
      self.kb = self.dialogue.kb
    if planGraph != None:
      self.planGraph = planGraph
    else:
      self.planGraph = self.dialogue.planGraph
    if executor != None:
      self.executor = executor
    else:
      self.executor = self.dialogue.executor
    self.type = "map"  # the type of generated response content (e.g. text message, map, etc...)
    f = open(os.path.dirname(__file__) +'/map.yaml')
    self.config = yaml.load(f)
    f.close()
    self.output_dir = self.config["output_dir"] + "/" + self.dialogue.id + "/" + self.id
    if not os.path.exists(self.output_dir):
      os.makedirs(self.output_dir)
    self.output_url = self.config["output_url"] + "/" + self.dialogue.id + "/" + self.id
    
  def getResponseContent(self):
    """return the generated content of this responder"""
    response = {}
    response["type"] = self.type
    response["content"] = self.executor.mapCtrl.saveXML()
    return response
  
  def __generateMapFile(self):
    """docstring for __generateMapFile"""
    # load the base map template
    mapnik_map_file = os.path.dirname(__file__) + "/" + self.config["mapnik_template_dir"] + "/basemap.xml"
    # do some modification to the map file
    m = mapnik.Map(256, 256, str(self.config["projection"]))
    mapnik.load_map(m, mapnik_map_file)
    
    lyr = mapnik.Layer('administrative', '+proj=latlong +datum=WGS84')
    lyr.datasource = mapnik.Shapefile(file=os.path.dirname(__file__) + "/" + self.config["data_dir"] + "/PA_Shape/pennsylvania_administrative")
    lyr.styles.append('admin')
    m.layers.append(lyr)
    # copy the map file to the output directory
    self.mapfile = str(self.output_dir+"/map.xml")
    mapnik.save_map(m, self.mapfile)
    #shutil.copy2(mapnik_map_file, self.mapfile)
  
  def __generatePreview(self):
    """docstring for __generatePreview"""
    width = self.config["preview"]["width"]
    height = self.config["preview"]["height"]
    m = mapnik.Map(width, height)
    mapnik.load_map(m, self.mapfile)
    prj = mapnik.Projection(self.config["projection"])
    c0 = prj.forward(mapnik.Coord(self.bbox[0],self.bbox[1]))
    c1 = prj.forward(mapnik.Coord(self.bbox[2],self.bbox[3]))
    m.zoom_to_box(mapnik.Envelope(c0.x, c0.y, c1.x, c1.y))
    img = mapnik.Image(width, height)
    mapnik.render(m, img)
    view = img.view(0, 0, width, height)
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + "." + self.config["preview"]["type"]
    view.save(str(self.output_dir + "/" + filename), str(self.config["preview"]["type"]))
    self.preview = self.output_url + "/" + filename      
    
  def generate(self):
    """generate the response"""
    # make decisions on the map scale, map layers
    #mockup
    #self.bbox = (-117, 25.0, -73, 51.0)
    #self.bbox = (-79.93, 39.19, -75.84, 41.92)
    self.bbox = (-77.97, 40.7, -77.75, 40.87)
    
    # generate the xml map file
    # 1. load the base map from the template and output it
    self.__generateMapFile()
    # 2. generate the static preview pictures
    self.__generatePreview()
    
    pass
    
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