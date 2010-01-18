#!/usr/bin/env python
# encoding: utf-8
"""
The class definition for DefaultResponder

Created by Bo Yu on 2010-01-02.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

class TextResponder():
  """the default responder, which outputs the result from the executor"""
  def __init__(self, id, dialogue, params = None):
    self.id = id
    self.dialogue = dialogue
    self.params = params
    self.kb = self.dialogue.kb
    self.planGraph = self.dialogue.planGraph
    self.executor = self.dialogue.executor
    self.type = "text"  # the type of generated response content (e.g. text message, map, etc...)

  def getResponseContent(self):
    """return the generated content of this responder"""
    response = {}
    response["type"] = self.type
    response["content"] = "Test message!"
    return response

  def generate(self):
    """generate the response"""
    pass
    
  def getResponse(self):
    """docstring for getResponse"""
    response = {}
    response["type"] = self.type
    response["id"] = self.id
    response["preview"] = "Test message!"  # the url of the preview map picture or summary of text content
    response["explanation"] = "the explanation of the response"
    return response
    
def main():
  pass

if __name__ == '__main__':
	main()