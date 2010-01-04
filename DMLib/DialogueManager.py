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

from PhoenixParser import *
from PlanGraph import *
from MapControl import *
from KBaseSqlite import *
from KBasePostgresql import *

def append_dir(dir):
  print dir
  sys.path.append(dir)

def check_validity(config):
  """check the validity of Config"""
  if config.has_key("context") and config.has_key("parser_dir") and config.has_key("kbase") and config.has_key("actuator_dir") and config.has_key("executor") and config.has_key("responders"):
    if len(config["responders"]) > 0:
      return True
  return False
  
class DialogueManager():
  """manage the dialogue process"""
  def __init__(self, config, id=""):
    if id:
      self.id = id
    else:
      # make a random id
      self.id = str(uuid.uuid4())
    self.participants = []
    if check_validity(config):
      self.context = config["context"]
      # create parser
      self.parser = PhoenixParser(self.context + config["parser_dir"] + "/config")
      # create knowledge base
      self.kb = self.__createKBase(config["kbase"])
      # add the actuator directory to PYTHONPATH
      append_dir(os.path.dirname(__file__) + "/../"  + self.context + config["actuator_dir"]) 
      # import the executor and create a new instance
      _executor = __import__(config["executor"]["module"])
      self.executor = getattr(_executor, config["executor"]["class"])()
      # create the plangraph
      self.planGraph = PlanGraph(kb=self.kb, executor=self.executor)
      # import all the responders and create new instances
      self.responders = []
      counter = 0
      for responder in config["responders"]:
        _responder = __import__(responder["module"])
        self.responders.append(getattr(_responder, responder["class"])(str(counter), self))
        counter = counter + 1
  
  def __createKBase(self, kbase):
    """docstring for create"""
    if kbase["type"] == "sqlite":
      return KBaseSqlite(self.context + kbase["dbfile"])
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
    # generate the responses    
    for responder in self.responders:
      responder.generate()
    return self.getResponses()
  
  def getPlanGraphXML(self):
    """docstring for getPlanGraphXML"""
    return self.planGraph.saveXML()
  
  def getResponseContent(self, responderId):
    """get the response content of a particular responder"""
    for responder in self.responders:
      if responder.id == responderId:
        return responder.getResponseContent()
    response = {}
    response["status"] = "error"
    response["message"] = "the responder (%s) does not exists!" % responderId
    return response
    
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

  def getResponses(self):
    """get the responses from all responders"""
    responses = []
    for responder in self.responders:
      response = responder.getResponse()
      if response:
        responses.append(response)
    if len(responses) == 0:
      response = {}
      response["status"] = "error"
      response["message"] = "there is no response at this moment!"
      return response
    return responses
    
def main():
  dlgManager = DialogueManager()
  request = Request("Jill", "There is a nuclear release, and we need to plan evacuation")
  print dlgManager.process(request)

if __name__ == '__main__':
	main()
