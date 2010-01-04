#!/usr/bin/env python
# encoding: utf-8
"""
The abstract class for Executor

Created by Bo Yu on 2010-01-02.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

class Executor():  
  def execute(self, plan):
    """execute the action represented by the given plan node"""
    if hasattr(self, plan.actionName):
      action = getattr(self, plan.actionName)
      action(plan)
        
def main():
  pass

if __name__ == '__main__':
	main()