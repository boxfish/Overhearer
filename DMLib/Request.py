#!/usr/bin/env python
# encoding: utf-8
"""
request message

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

class Request():
  """model the participant"""
  def __init__(self, speaker="", message=""):
    self.properties = ("message", "speaker")
    self.message = message
    self.speaker = speaker
  
  def __repr__(self):
    """docstring for __repr__"""
    return "(" + ",".join(["%s=%s" % (attr, getattr(self, attr)) for attr in self.properties if hasattr(self, attr)] ) + ")"
    
def main():
  pass

if __name__ == '__main__':
	main()