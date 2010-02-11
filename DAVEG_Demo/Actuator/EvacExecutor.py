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
      if not paramValue in plan.generatedValues:
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
      if not plan.refPhrase in plan.parent.values:
        plan.parent.values.append(plan.refPhrase)
        plan.parent.status = param_status_hasValue
      plan.mentalState.execStatus = exec_success
      values = {}
      values["name"] = str(plan.refPhrase) + ' mile epz'
      values["type"] = "structure"
      values["styles"] = ['_'.join(values["name"].split(' ')),]
      self.mapCtrl.addMapLayer(values)
      if not values["name"] in plan.generatedValues:
        plan.generatedValues.append(values["name"])
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
        if not values["name"] in plan.generatedValues:
          plan.generatedValues.append(values["name"])
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
      if not values["name"] in plan.generatedValues:
        plan.generatedValues.append(values["name"])

  def PerformEvacuation(self, plan):
    """docstring for PerformEvacuation"""
    print "Execute: PerformEvacuation"
    action = plan.parent.searchActionsByName("GenerateEPZZone")[0]
    iden_actions = action.searchActionsByName("IdentifyQuantityFromSpeech")
    for ident_action in iden_actions:
      for value in ident_action.generatedValues:
        self.mapCtrl.removeMapLayer(value)
    self.mapCtrl.removeMapLayer('plume model')
    values = {}
    values["name"] = 'evacuation area'
    values["type"] = "structure"
    values["styles"] = ['_'.join(values["name"].split(' ')),]
    self.mapCtrl.addMapLayer(values)  
    self.mapCtrl.setMapExtent(-8560082.0, 4869277.0,-8513847.0, 4907464.5)
    if not values["name"] in plan.generatedValues:
      plan.generatedValues.append(values["name"])          
    plan.mentalState.execStatus = exec_success
    plan.searchParamByName("ImpactedArea").status = param_status_success

  def IdentifyDiffLocFromGesture(self, plan):
    print "Execute: IdentifyDiffLocFromGesture"
    if plan.refGestures:
      center = self.GetCenterPoint(plan.refGestures)
      width = 0.5 * (self.mapCtrl.bbox[2] - self.mapCtrl.bbox[0])
      height = 0.5 * (self.mapCtrl.bbox[3] - self.mapCtrl.bbox[1])
      minX = center[0] - 0.5 * width
      minY = center[1] - 0.5 * height
      maxX = center[0] + 0.5 * width
      maxY = center[1] + 0.5 * height
      self.mapCtrl.setMapExtent(minX, minY, maxX, maxY)
  
  def AssignGuideTeam(self, plan):
    print "Execute: AssignGuideTeam"
    if plan.refGestures:
      center = self.GetCenterPoint(plan.refGestures)
      print "TEST"
      layer = self.mapCtrl.getMapLayer('guide team')
      print layer
      if not layer:
        values = {}
        values["name"] = "guide team"
        values["type"] = "points"
        values["styles"] = ['_'.join(values["name"].split(' ')),]
        values["values"] = []
        print values
        values["values"].append({"coords": center, "label":plan.agents[0].id})
        print "AddLayer"
        self.mapCtrl.addMapLayer(values)
        print "AddLayer successfully!"
      else:
        layer["values"].append({"coords": center, "label":plan.initiator.id})
        
  def GetCenterPoint(self, gestures):
    minX = gestures[0][0][0]
    maxX = gestures[0][0][0]
    minY = gestures[0][0][1]
    maxY = gestures[0][0][1]
    for gesture in gestures:
      for point in gesture:
        if point[0] < minX:
          minX = point[0]    
        if point[0] > maxX:
          maxX = point[0]
        if point[1] < minY:
          minY = point[1]    
        if point[1] > maxY:
          maxY = point[1]
    return [0.5*(minX + maxX), 0.5*(minY + maxY)]
          
def main():
  pass
  
if __name__ == '__main__':
	main()