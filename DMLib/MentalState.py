#!/usr/bin/env python
# encoding: utf-8
"""
Mental States of a participant

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

# intention
(int_unknown, int_intendTo, int_intendThat, int_intendNot, int_potential) = range (5)
int_status = ["int_unknown", "int_intendTo", "int_intendThat", "int_intendNot", "int_potential"]
# status of plans
(exec_noRecipe, exec_hasRecipe, exec_canBringAbout, exec_paramReady, exec_success, exec_failure) = range(6)
exec_status = ["exec_noRecipe", "exec_hasRecipe", "exec_canBringAbout", "exec_paramReady", "exec_success", "exec_failure"] 
# types of parameters
(param_type_unknown, param_type_geoType, param_type_int, param_type_real, param_type_text) = range(5)
param_type = ["param_type_unknown", "param_type_geoType", "param_type_int", "param_type_real", "param_type_text"]
# status of parameters
(param_status_notReady, param_status_hasValue, param_status_success, param_status_fail) = range(4)
param_status = ["param_status_notReady", "param_status_hasValue", "param_status_success", "param_status_fail"]

class MentalState():
  """model the plan graph"""
  def __init__(self):
    self.properties = ("intention", "execStatus")
    self.intention = int_unknown
    self.execStatus = exec_noRecipe

  def __repr__(self):
    """docstring for __repr__"""
    return "(" + ",".join(["%s=%s" % (attr, getattr(self, attr)) for attr in self.properties if hasattr(self, attr)] ) + ")"
    
def main():
  pass

if __name__ == '__main__':
	main()