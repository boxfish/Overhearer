#!/usr/bin/env python
# encoding: utf-8
"""
The abstract class for Responder

Created by Bo Yu on 2010-01-02.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

class Responder():
  """the abstract class of an responder, which generate response based on plangraph and executing status"""
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
    self.type = ""  # the type of generated response content (e.g. text message, map, etc...)
  
  def getResponseContent(self):
    """return the generated content of this responder"""
    pass      
    
def main():
  pass

if __name__ == '__main__':
	main()