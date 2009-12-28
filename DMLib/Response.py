#!/usr/bin/env python
# encoding: utf-8
"""
response message

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

class Response():
  """model the participant"""
  def __init__(self, message="", status="unknown"):
    self.properties = ("message", "status", "planGraph")
    self.message = message
    self.status = status
    self.planGraph = ""
  
  def __repr__(self):
    """docstring for __repr__"""
    return "(" + ",".join(["%s=%s" % (attr, getattr(self, attr)) for attr in self.properties if hasattr(self, attr)] ) + ")"
    
def main():
  pass

if __name__ == '__main__':
	main()