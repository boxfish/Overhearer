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
        
                
class EvacResponder():
    """the default map responder, which outputs the result from the executor"""
    def __init__(self, dialogue, params=None):
        self.dialogue = dialogue
        self.params = params
        self.kb = self.dialogue.kb
        self.planGraph = self.dialogue.planGraph
        self.executor = self.dialogue.executor
        self.type = "map"    # the type of generated response content (e.g. text message, map, etc...)
        self.id = "0"
        self.map_width = 450
        self.map_height = 450
        self.bbox = []
    
    def getResponseContent(self, responseId):
        """return the generated content of this responder"""
        response = {}
        response["type"] = self.type
        response["content"] = self.preview
        return response
    
    def getResponseChannels(self):
        """docstring for getResponseChannels"""
        channels = []
        resp = {}
        resp["id"] = self.id
        resp["type"] = self.type
        resp["name"] = "DAVEG_Demo" 
        channels.append(resp)
        return channels
    
    def getCurrentResponses(self):
        """docstring for getCurrentResponses"""
        return [self.getResponse(),]            
        
    def generate(self):
        """generate the response"""
        self.preview = self.executor.mapCtrl.generateStaticMap(self.map_width, self.map_height)
        self.bbox = self.executor.mapCtrl.bbox
        
    def getResponse(self):
        """docstring for getResponse"""
        response = {}
        response["type"] = self.type
        response["id"] = self.id
        response["preview"] = self.preview  # the url of the preview map picture
        response["explanation"] = "the explanation of the response"
        response["bbox"] = ",".join(self.bbox)
        return response
        
def main():
       pass

if __name__ == '__main__':
    main()