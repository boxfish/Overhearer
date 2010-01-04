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
local_dir = os.path.dirname(__file__)
DMLib_dir = local_dir + "/../../DMLib"
sys.path.append(local_dir)
sys.path.append(DMLib_dir)    
    
from MentalState import *
from Executor import Executor

from MapControl import OLMapControl

#BASE_URL = 'http://spatiallab.ist.psu.edu:8080'
BASE_URL = 'http://localhost:8080'

class EvacExecutor(Executor):
  """docstring for ClassName"""
  def __init__(self):
    self.mapCtrl = OLMapControl(os.path.dirname(__file__) + "/MapTemplates/basemap.xml")

  def IdentifyFeatureFromSpeech(self, plan):
    """docstring for IdentifyFeatureFromSpeech"""
    print "Execute: IdentifyFeatureFromSpeech: %s" % plan.refPhrase
    # mockup: get the feature based on phrase
    paramValue = plan.refPhrase
    # mockup: decide the map extent
    minx = -11701506.82
    miny = 4795957.865
    maxx = -11630573.26
    maxy = 4865515.560
    self.mapCtrl.setMapExtent(minx, miny, maxx, maxy)
    # update plan graph
    if paramValue:
      plan.parent.values.append(paramValue)
      plan.parent.status = param_status_hasValue
      plan.mentalState.execStatus = exec_success
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
      plan.parent.values.append(paramValue)
      plan.parent.status = param_status_hasValue
      plan.mentalState.execStatus = exec_success
    else:
      plan.mentalState.execStatus = exec_failure

  def CalculateBufferZone(self, plan):
    """docstring for CalculateBufferZone"""
    print "Execute: CalculateBufferZone"
    paramLoc = plan.searchParamByName("IncidenceLocation")
    paramDist = plan.searchParamByName("Distance")
    if paramLoc and paramDist and len(paramLoc.values) > 0 and len(paramDist.values) > 0:
      # calculate the buffer zones
      self.mapCtrl.removeMapLayer("20EPZ");
      self.mapCtrl.removeMapLayer("30EPZ");
      self.mapCtrl.removeMapLayer("40EPZ");
      for dist in paramDist.values:
        values = {}
        values["name"] = str(dist) + 'EPZ'
        values["title"] = values["name"]
        values["url"] = BASE_URL + '/static/data/' + values["name"] + '.kml'
        self.mapCtrl.addMapLayer('kml', values)
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
      values["name"] = 'Plume'
      values["title"] = values["name"]
      values["url"] = BASE_URL + '/static/data/Plume.kml'
      self.mapCtrl.addMapLayer('kml', values)
      plan.mentalState.execStatus = exec_success
      plan.searchParamByName("ImpactedArea").status = param_status_hasValue

  def PerformEvacuation(self, plan):
    """docstring for PerformEvacuation"""
    print "Execute: PerformEvacuation"
    plan.mentalState.execStatus = exec_success
    plan.searchParamByName("ImpactedArea").status = param_status_success

def main():
  pass
  
if __name__ == '__main__':
	main()