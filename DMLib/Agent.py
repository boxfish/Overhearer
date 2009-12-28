#!/usr/bin/env python
# encoding: utf-8
"""
a participant

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

from MentalState import *

class Agent():
  """model the participant"""
  def __init__(self, id):
    self.properties = ("id", "mentalState")
    self.id = id
    self.mentalState = MentalState()
  
  def __repr__(self):
    """docstring for __repr__"""
    return "(" + ",".join(["%s=%s" % (attr, getattr(self, attr)) for attr in self.properties if hasattr(self, attr)] ) + ")"
    
def main():
  pass

if __name__ == '__main__':
	main()