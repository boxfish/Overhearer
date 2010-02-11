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
import mapnik
import datetime

class MapnikControl():
    """model the map control"""
    def __init__(self, base_map_file, output_base_dir, output_base_url, projection):
        self.base_map_file = str(base_map_file)
        self.output_base_dir = str(output_base_dir)
        self.output_base_url = str(output_base_url)
        self.projection = str(projection)
        self.bbox = [-13852053.638602437, 933101.2722854596, -4975574.699678951, 7526228.245446581]
        self.mapContents = {}
    
    def sortMapContents(self):
        order_list = ["ten mile epz", "five mile epz", "two mile epz", "plume model", "evacuation area", "three mile island nuclear station", "guide team"]
        newMapContents = []
        for layer_name in order_list:
            if layer_name in self.mapContents:
                newMapContents.append(layer_name)
        return newMapContents
        
    def generateStaticMap(self, width, height):
        """docstring for getMapXML"""
        dt = datetime.datetime.now()
        timestamp = dt.strftime("%Y-%m-%d-%H-%M-%S") + "-" + str(dt.microsecond)
        img_file = os.path.join(self.output_base_dir, "%s.png" % timestamp)
        img = None
        m = mapnik.Map(width, height)
        mapnik.load_map(m, self.base_map_file)
        env = mapnik.Envelope(self.bbox[0], self.bbox[1], self.bbox[2], self.bbox[3])
        m.zoom_to_box(env)
        layer_names = self.sortMapContents()
        for layer_name in layer_names:
            layer_info = self.mapContents[layer_name]
            layer_type = layer_info.get("type", "")
            if layer_type and layer_type != "layer":
                lyr = mapnik.Layer(layer_name, self.projection)
                if layer_type == "points":
                    lyr.datasource = mapnik.PointDatasource()
                    for value in layer_info.get("values", []):
                        lyr.datasource.add_point(value["coords"][0], value["coords"][1], "label", value["label"])
                        print value
                else:
                    # add the layer & styles
                    query = "(select geom, label from geo_contents where name='%s') as %s" % (layer_name, '_'.join(layer_name.split(' ')))
                    lyr.datasource = mapnik.PostGIS(host='localhost',user='admin',password='309ist',dbname='nuclear_release',table=query)
                styles = layer_info.get("styles", [])
                for style in styles:
                    lyr.styles.append(style)
                m.layers.append(lyr)
                #mapnik.save_map(m,os.path.join(self.output_base_dir, "temp.xml"))
        img = mapnik.Image(width, height)
        mapnik.render(m, img)
        img.save(img_file, "png")
        if img:
            return "%s/%s.png" % (self.output_base_url, timestamp)
        else:
            return None
  
    def setMapExtent(self, minx, miny, maxx, maxy):
        self.bbox = [minx, miny, maxx, maxy]
    
    def addMapLayer(self, values):            
        if values and "name" in values:
            newLayerName = values["name"]
            content = self.mapContents.get(newLayerName, {})
            if not content:
                self.mapContents[newLayerName] = values
  
    def removeMapLayer(self, layerName):
        if layerName in self.mapContents:
            del self.mapContents[layerName]
        return
    
    def removeEPZLayers(self):
        for layer_name in self.mapContents.keys():
            if layer_name.endswith(" epz"):
                del self.mapContents[layer_name]
        
    def removeFocusLayers(self):
        """docstring for removeFocusLayer"""
        for layer_name, layer_info in self.mapContents.items():
            styles = layer_info.get("styles", [])
            for style in styles:
                if style.endswith("_focus"):
                    self.mapContents[layer_name]["styles"].remove(style)
    
    def addFocusLayer(self, layerName):
        if layerName in self.mapContents:
            styles = self.mapContents[layerName].get("styles", [])
            for style in styles:
                if style.endswith("_focus"):
                    return
            self.mapContents[layerName]["styles"].append('_'.join(layerName.split(' '))+'_focus')    

    def getMapLayer(self, layerName):
        if layerName in self.mapContents:
            return self.mapContents[layerName]
        else:
            return None
            
def main():
    pass
    
if __name__ == '__main__':
	main()