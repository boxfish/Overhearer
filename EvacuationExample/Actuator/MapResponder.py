#!/usr/bin/env python
# encoding: utf-8
"""
The class definition for MapResponder

Created by Bo Yu on 2010-01-02.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

class MapResponder():
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
  
  def getResponseContent(self):
    """return the generated content of this responder"""
    response = {}
    response["type"] = self.type
    response["content"] = self.executor.mapCtrl.saveXML()
    return response

  def generate(self):
    """generate the response"""
    pass
    
  def getResponse(self):
    """docstring for getResponse"""
    response = {}
    response["type"] = self.type
    response["id"] = self.id
    response["preview"] = "/static/images/1.jpg"  # the url of the preview map picture
    response["explanation"] = "the explanation of the response"
    return response
    
def main():
  pass

if __name__ == '__main__':
	main()