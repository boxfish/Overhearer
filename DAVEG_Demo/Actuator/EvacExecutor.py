#!/usr/bin/env python
# encoding: utf-8
"""
domain specific basic actions

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os

# append the DMLib and local directories to PYTHONPATH
#local_dir = os.path.dirname(__file__)
#DMLib_dir = local_dir + "/../../DMLib"
#sys.path.append(local_dir)
#sys.path.append(DMLib_dir)    
    
from Overhearer.DMLib.MentalState import *
from Overhearer.DMLib.Executor import Executor

#from MentalState import *
#from Executor import Executor
from MapnikControl import MapnikControl
import yaml

class EvacExecutor(Executor):
  """docstring for ClassName"""
  def __init__(self, params):
    f = open(os.path.join(os.path.dirname(__file__), 'map.yaml'))
    config = yaml.load(f)
    f.close()
    self.output_base_dir = os.path.join(config["output_base_dir"])
    self.base_map_file = os.path.join(config["base_map_file"])
    self.output_base_url = os.path.join(config["output_base_url"])
    self.projection = os.path.join(config["projection"])
    self.mapCtrl = MapnikControl(self.base_map_file, self.output_base_dir, self.output_base_url, self.projection)
    self.params = params

  def IdentifyFeatureFromSpeech(self, plan):
    """docstring for IdentifyFeatureFromSpeech"""
    print "Execute: IdentifyFeatureFromSpeech: %s" % plan.refPhrase
    # mockup: get the feature based on phrase
    paramValue = plan.refPhrase
    
    # mockup: decide the map extent
    if paramValue == "three mile island nuclear station":
        self.mapCtrl.setMapExtent(-8574408.602598343, 4855651.740543485, -8508086.231095564, 4918399.766340519)
        values = {}
        values["name"] = paramValue
        values["type"] = "location"
        values["styles"] = ['_'.join(values["name"].split(' ')),]
        self.mapCtrl.addMapLayer(values)
    else:
        self.mapCtrl.setMapExtent(-8854449.813570915, 4830153.383535952, -8476288.5977869, 5159633.330083089)    
    # update plan graph
    if paramValue:
      plan.parent.values.append(paramValue)
      plan.parent.status = param_status_hasValue
      plan.mentalState.execStatus = exec_success
      plan.generatedValues.append(paramValue)
    else:
      plan.mentalState.execStatus = exec_failure

  def IdentifyQuantityFromSpeech(self, plan):
    print "Execute: IdentifyQuantityFromSpeech: %s" % plan.refPhrase
    if plan.refPhrase == "one":
      paramValue = 1
    elif plan.refPhrase == "two":
      paramValue = 2   
    elif plan.refPhrase == "three":
      paramValue = 3   
    elif plan.refPhrase == "four":
      paramValue = 4   
    elif plan.refPhrase == "five":
      paramValue = 5   
    elif plan.refPhrase == "six":
      paramValue = 6   
    elif plan.refPhrase == "seven":
      paramValue = 7   
    elif plan.refPhrase == "eight":
      paramValue = 8   
    elif plan.refPhrase == "nine":
      paramValue = 9   
    elif plan.refPhrase == "ten":
      paramValue = 10   
    elif plan.refPhrase == "twenty":
      paramValue = 20   
    elif plan.refPhrase == "thirty":
      paramValue = 30   
    elif plan.refPhrase == "forty":
      paramValue = 40   
    elif plan.refPhrase == "fifty":
      paramValue = 50
    else:
      paramValue = -1
    # update plan graph
    if paramValue >=0:
      plan.parent.values.append(plan.refPhrase)
      plan.parent.status = param_status_hasValue
      plan.mentalState.execStatus = exec_success
      plan.generatedValues.append(plan.refPhrase)
      values = {}
      values["name"] = str(plan.refPhrase) + ' mile epz'
      values["type"] = "structure"
      values["styles"] = ['_'.join(values["name"].split(' ')),]
      self.mapCtrl.addMapLayer(values)
      plan.searchParamByName("ImpactedArea").status = param_status_hasValue
    else:
      plan.mentalState.execStatus = exec_failure

  def CalculateBufferZone(self, plan):
    """docstring for CalculateBufferZone"""
    print "Execute: CalculateBufferZone"
    paramLoc = plan.searchParamByName("IncidenceLocation")
    paramDist = plan.searchParamByName("Distance")
    if paramLoc and paramDist and len(paramLoc.values) > 0 and len(paramDist.values) > 0:
      # calculate the buffer zones
      for dist in paramDist.values:
        values = {}
        values["name"] = str(dist) + ' mile epz'
        values["type"] = "structure"
        values["styles"] = ['_'.join(values["name"].split(' ')),]
        self.mapCtrl.addMapLayer(values)
      plan.mentalState.execStatus = exec_success
      plan.searchParamByName("ImpactedArea").status = param_status_hasValue

  def GetCurrentWindCondition(self, plan):
    """docstring for GetCurrentWindCondition"""
    print "Execute: GetCurrentWindCondition"
    plan.parent.values.append("current wind condition")
    plan.parent.status = param_status_hasValue
    plan.mentalState.execStatus = exec_success
    self.CalculatePlumeModel(plan)

  def CalculatePlumeModel(self, plan):
    print "Execute: CalculatePlumeModel"
    paramLoc = plan.searchParamByName("IncidenceLocation")
    if paramLoc and len(paramLoc.values) > 0:
      # calculate plumen model
      values = {}
      values["name"] = 'plume model'
      values["type"] = "structure"
      values["styles"] = ['_'.join(values["name"].split(' ')),]
      self.mapCtrl.addMapLayer(values)
      plan.mentalState.execStatus = exec_success
      plan.searchParamByName("ImpactedArea").status = param_status_hasValue

  def PerformEvacuation(self, plan):
    """docstring for PerformEvacuation"""
    print "Execute: PerformEvacuation"
    action = plan.parent.searchActionsByName("GenerateEPZZone")[0]
    iden_actions = action.searchActionsByName("IdentifyQuantityFromSpeech")
    for ident_action in iden_actions:
      for value in ident_action.generatedValues:
        self.mapCtrl.removeMapLayer(str(value) + ' mile epz')
    self.mapCtrl.removeMapLayer('plume model')
    values = {}
    values["name"] = 'evacuation area'
    values["type"] = "structure"
    values["styles"] = ['_'.join(values["name"].split(' ')),]
    self.mapCtrl.addMapLayer(values)            
    plan.mentalState.execStatus = exec_success
    plan.searchParamByName("ImpactedArea").status = param_status_success

def main():
  pass
  
if __name__ == '__main__':
	main()