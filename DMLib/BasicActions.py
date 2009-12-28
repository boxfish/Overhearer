#!/usr/bin/env python
# encoding: utf-8
"""
domain specific basic actions

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os
from MentalState import *

def execute(plan, map):
  """docstring for execute"""
  module = sys.modules[__name__]
  action = getattr(module, plan.actionName)
  action(plan, map)
    
def IdentifyFeatureFromSpeech(plan, map):
  """docstring for IdentifyFeatureFromSpeech"""
  print "Execute: IdentifyFeatureFromSpeech: %s" % plan.refPhrase
  # mockup: get the feature based on phrase
  paramValue = plan.refPhrase
  # mockup: decide the map extent
  minx = -11701506.82
  miny = 4795957.865
  maxx = -11630573.26
  maxy = 4865515.560
  map.setMapExtent(minx, miny, maxx, maxy)
  # update plan graph
  if paramValue:
    plan.parent.values.append(paramValue)
    plan.parent.status = param_status_hasValue
    plan.mentalState.execStatus = exec_success
  else:
    plan.mentalState.execStatus = exec_failure

def IdentifyQuantityFromSpeech(plan, map):
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
    plan.parent.values.append(paramValue)
    plan.parent.status = param_status_hasValue
    plan.mentalState.execStatus = exec_success
  else:
    plan.mentalState.execStatus = exec_failure

def CalculateBufferZone(plan, map):
  """docstring for CalculateBufferZone"""
  print "Execute: CalculateBufferZone"
  paramLoc = plan.searchParamByName("IncidenceLocation")
  paramDist = plan.searchParamByName("Distance")
  if paramLoc and paramDist and len(paramLoc.values) > 0 and len(paramDist.values) > 0:
    # calculate the buffer zones
    map.removeMapLayer("20EPZ");
    map.removeMapLayer("30EPZ");
    map.removeMapLayer("40EPZ");
    for dist in paramDist.values:
      values = {}
      values["name"] = str(dist) + 'EPZ'
      values["title"] = values["name"]
      values["url"] = '/static/data/' + values["name"] + '.kml'
      map.addMapLayer('kml', values)
    
    plan.mentalState.execStatus = exec_success
    plan.searchParamByName("ImpactedArea").status = param_status_hasValue

def GetCurrentWindCondition(plan, map):
  """docstring for GetCurrentWindCondition"""
  print "Execute: GetCurrentWindCondition"
  plan.parent.values.append("current wind condition")
  plan.parent.status = param_status_hasValue
  plan.mentalState.execStatus = exec_success
  CalculatePlumeModel(plan, map)

def CalculatePlumeModel(plan, map):
  print "Execute: CalculatePlumeModel"
  paramLoc = plan.searchParamByName("IncidenceLocation")
  if paramLoc and len(paramLoc.values) > 0:
    # calculate plumen model
    values = {}
    values["name"] = 'Plume'
    values["title"] = values["name"]
    values["url"] = '/static/data/Plume.kml'
    map.addMapLayer('kml', values)
    plan.mentalState.execStatus = exec_success
    plan.searchParamByName("ImpactedArea").status = param_status_hasValue

def PerformEvacuation(plan, map):
  """docstring for PerformEvacuation"""
  print "Execute: PerformEvacuation"
  plan.mentalState.execStatus = exec_success
  plan.searchParamByName("ImpactedArea").status = param_status_success
  pass

def main():
  execute(None, None)

if __name__ == '__main__':
	main()