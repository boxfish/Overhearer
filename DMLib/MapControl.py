#!/usr/bin/env python
# encoding: utf-8
"""
control the map display

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os
import xml.dom.minidom as minidom
import web

class OLMapControl():
  """model the map control"""
  def __init__(self, baseMapFile):
    self.baseMapFile = baseMapFile
    self.xmldoc = minidom.parse(baseMapFile)
    self.layers = []
    layerList = self.xmldoc.getElementsByTagName('LayerList')[0].getElementsByTagName('Layer')
    for layer in layerList:
      name = str(layer.getElementsByTagName('Name')[0].firstChild.data)
      self.layers.append(name)
    
  def saveXML(self):
    """docstring for getMapXML"""
    return self.xmldoc.toxml()
  
  def setMapExtent(self, minx, miny, maxx, maxy):
    generalSec = self.xmldoc.getElementsByTagName('General')[0]
    bbox = generalSec.getElementsByTagName('BoundingBox')[0]
    bbox.setAttribute('minx', str(minx))
    bbox.setAttribute('miny', str(miny))
    bbox.setAttribute('maxx', str(maxx))
    bbox.setAttribute('maxy', str(maxy))
  
  def addMapLayer(self, type, values):
    if values and values.has_key("name"):
      newLayerName = values["name"]
      if newLayerName in self.layers:
        return
      else:  
        render = web.template.render(os.path.dirname(self.baseMapFile) + '/MapTemplates')
        layerRender = getattr(render, type)
        newLayer = minidom.parseString(str(layerRender(values))).documentElement
        layerListSec = self.xmldoc.getElementsByTagName('LayerList')[0]
        layerListSec.appendChild(newLayer)
        self.layers.append(newLayerName)
  
  def removeMapLayer(self, layerName):
    if layerName in self.layers:
      layerListSec = self.xmldoc.getElementsByTagName('LayerList')[0]
      layerList = layerListSec.getElementsByTagName('Layer')
      for layer in layerList:
        name = str(layer.getElementsByTagName('Name')[0].firstChild.data)
        if name == layerName:
          layerListSec.removeChild(layer)
          self.layers.remove(layerName)
          return
      
            
  def __repr__(self):
    """docstring for __repr__"""
    return "(" + ",".join(["%s=%s" % (attr, getattr(self, attr)) for attr in self.properties if hasattr(self, attr)] ) + ")"

def main():
  pass

if __name__ == '__main__':
	main()