#!/usr/bin/env python
# encoding: utf-8
"""
Dialogue Manager

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os
import copy
import xml.dom.minidom as minidom
import uuid

from Request import *
from Response import *
from PhoenixParser import *
from PlanGraph import *
from MapControl import *
from KBaseSqlite import *
from KBasePostgresql import *


class DialogueManager():
  """manage the dialogue process"""
  def __init__(self, config, id=""):
    if id:
      self.id = id
    else:
      # make a random id
      self.id = str(uuid.uuid4())
    if config.has_key("context") and config.has_key("kbase"):
      #context = "EvacuationExample"
      self.parser = PhoenixParser(config["context"] + "/config")
      self.participants = []
      #self.kb = KnowledgeBase(context + "/kboop.sqlite")
      self.kb = self.__createKBase(config["kbase"])
      self.mapCtrl = OLMapControl(config["context"] + "/basemap.xml")
      self.planGraph = PlanGraph(kb=self.kb, mapCtrl=self.mapCtrl)
  
  def __createKBase(self, kbase):
    """docstring for create"""
    if kbase["type"] == "sqlite":
      return KBaseSqlite(kbase["fname"])
    elif kbase["type"] == "postgresql":
      dsn = " ".join(["%s=%s" % (k, v) for k, v in kbase.items() if k != "type"])
      return KBasePostgresql(dsn)
    else:
      return None
            
  def addParticipant(self, newParticipant):
    """docstring for addParticipant"""
    if newParticipant.has_key("id"):
      for participant in self.participants:
        if participant["id"] == newParticipant["id"]:
          return
      self.participants.append(newParticipant)
    
  def process(self, request):
    """process the incoming message"""
    response = {}
    #request["message"] = request["message"].encode('ASCII')
    #print request
    # Step 1: Parsing
    # parse message into phrases
    result = self.parser.parse(request["message"])
    # parse phrases to tempPlans
    tempPlans = self.planGraph.parsePhrases(result["phrases"], request["speakerId"])
    # if no phrases are parsed, return the error message
    if len(tempPlans) == 0:
      response["status"] = "error"
      response["message"] = "could not parse the request."
      return response
    # Step 2: Explaining
    self.planGraph.explain(tempPlans)
    if len(self.planGraph.focus) == 0:
      response["status"] = "error"
      response["message"] = "could not explain the request."
      return response
    # Step 3: Elaborating
    self.planGraph.elaborate()
    # Step 4: Geenrating Response
    # generate the response message
    return self.__generateResponse()
  
  def getPlanGraphXML(self):
    """docstring for getPlanGraphXML"""
    return self.planGraph.saveXML()
  
  def getMapXML(self):
    """docstring for getMapXML"""
    """
    # test purpose
    self.mapCtrl.setMapExtent('-10', '-10', '10', '10')
    values = {}
    values["name"] = 'test'
    values["title"] = 'test'
    values["url"] = 'test.kml'
    self.mapCtrl.addMapLayer('kml', values)
    self.mapCtrl.removeMapLayer('test')
    """
    return self.mapCtrl.saveXML()

  def __generateResponse(self):
    """docstring for __generateResponse"""
    response = {}
    response["status"] = "success"
    return response
    
def main():
  dlgManager = DialogueManager()
  request = Request("Jill", "There is a nuclear release, and we need to plan evacuation")
  print dlgManager.process(request)

if __name__ == '__main__':
	main()
