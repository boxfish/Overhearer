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
 sys.path.append(dir)

class DialogueManager():
    """manage the dialogue process"""
    def __init__(self, config, id=""):
        if id:
            self.id = id
        else:
            # make a random id
            self.id = str(uuid.uuid4())
        self.participants = []
        self.config = config
        if self.config:
            self.context = self.config["context"]
            # create parser
            self.parser = PhoenixParser(self.context + self.config["parser_dir"] + "/config")
            
            # create knowledge base
            self.kb = self.__createKBase(self.config["kbase"])

            # add the actuator directory to PYTHONPATH
            #self.actuator_dir = os.path.join(os.path.dirname(__file__), "..", self.context, self.config["actuator_dir"])
            #sys.path.append(self.actuator_dir)
            #append_dir(os.path.dirname(__file__) + "/../"    + self.context + self.config["actuator_dir"]) 
            #_executor = __import__(self.config["executor"]["module"])

            # import the executor and create a new instance
            executor_module_name = ".".join(["Overhearer", self.context, self.config["executor"]["module"]])
            __import__(executor_module_name) 
            _executor = sys.modules[executor_module_name]
            executor_params = self.config["executor"].get("params", None)
            self.executor = getattr(_executor, self.config["executor"]["class"])(executor_params)
            # create the plangraph
            self.planGraph = PlanGraph(kb=self.kb, executor=self.executor)
            # import all the responders and create new instances
            self.responders = []
            for i, responder in enumerate(self.config["responders"]):
                responder_module_name = ".".join(["Overhearer", self.context, responder["module"]])
                __import__(responder_module_name)
                _responder = sys.modules[responder_module_name]
                responder_params = responder.get("params", None)
                self.responders.append(getattr(_responder, responder["class"])(str(i), self, responder_params))
    
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
        pId = newParticipant.get("id", "")
        if pId:
            for participant in self.participants:
                if participant["id"] == pId:
                    return False
            self.participants.append(newParticipant)
            return True
        else:
            return False
                    
    def process(self, request):
        """process the incoming message"""
        response = {}
        speakerId = request.get("speakerId", "")
        message = request.get("message", "")
        if speakerId == "" or message == "":
                response["status"] = "error"
                response["message"] = "the message cannot be processed!"
                return response
        # Step 1: Parsing
        # parse message into phrases
        result = self.parser.parse(message)
        # parse phrases to tempPlans
        tempPlans = self.planGraph.parsePhrases(result["phrases"], speakerId)
        
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
        return self.getCurrentResponses()
    
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

    def getResponders(self):
        """get the information about all the responders"""
        responders = []
        for responder in self.responders:
            resp = {}
            resp["id"] = responder.id
            resp["type"] = responder.type
            resp["name"] = responder.__class__.__name__ 
            responders.append(resp)
        return responders
        
    def getCurrentResponses(self):
        """get the current responses from all responders"""
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
