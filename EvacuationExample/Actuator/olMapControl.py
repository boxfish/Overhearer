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
from genshi.template import TemplateLoader
import mapnik

MERC_PROJ4 = "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over"

class olMapControl():
    """model the map control"""
    def __init__(self, ol_template_dir):
        self.ol_template_dir = ol_template_dir
        baseMapFile = os.path.join(ol_template_dir, "basemap.xml")
        self.xmldoc = minidom.parse(baseMapFile)
        self.layers = []
        layerList = self.xmldoc.getElementsByTagName('LayerList')[0].getElementsByTagName('Layer')
        for layer in layerList:
            name = str(layer.getElementsByTagName('Name')[0].firstChild.data)
            self.layers.append(name)
        self.mercator = mapnik.Projection(MERC_PROJ4)
        
    def saveXML(self):
        """docstring for getMapXML"""
        return self.xmldoc.toxml()
    
    def setMapExtent(self, minx, miny, maxx, maxy):
        lonlat_bbox = mapnik.Envelope(minx,miny,maxx,maxy)
        env = self.mercator.forward(lonlat_bbox)
        generalSec = self.xmldoc.getElementsByTagName('General')[0]
        bbox = generalSec.getElementsByTagName('BoundingBox')[0]
        bbox.setAttribute('minx', str(env.minx))
        bbox.setAttribute('miny', str(env.miny))
        bbox.setAttribute('maxx', str(env.maxx))
        bbox.setAttribute('maxy', str(env.maxy))
    
    def addMapLayer(self, type, layerInfo):
        if layerInfo:
            newLayerName = layerInfo.get("name", "")
            if newLayerName:
                if newLayerName in self.layers:
                    # remove it first
                    self.removeMapLayer(newLayerName)
                layer_loader = TemplateLoader(self.ol_template_dir, auto_reload=False)
                layer_tmpl = layer_loader.load('%s.xml' % type)
                layer_string = layer_tmpl.generate(layerInfo=layerInfo).render()
                newLayer = minidom.parseString(layer_string).documentElement
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

                        
def main():
    pass

if __name__ == '__main__':
    main()