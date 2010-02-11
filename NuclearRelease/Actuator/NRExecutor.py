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
import psycopg2
                
class NRExecutor(Executor):
    """docstring for ClassName"""
    def __init__(self, params=None):
        self.params = params
        if self.params and self.params.get("datasource", ""):
            self.datasource = self.params["datasource"]
            if self.datasource.get("type", "") == "postgresql":
                self.dsn = " ".join(["%s=%s" % (k, v) for k, v in self.datasource.items() if k != "type"])
        else:
            self.datasource = None

    def IdentifyLocationFromSpeech(self, plan):
        """docstring for IdentifyLocationFromSpeech"""
        print "Execute: IdentifyLocationFromSpeech: %s" % plan.refPhrase
        paramValue = ""
        # only support postgresql right now
        if self.datasource and self.datasource.get("type", "") == "postgresql":
            db = psycopg2.connect(self.dsn)
            cursor = db.cursor()
            query = "SELECT name FROM geo_contents where name = '%s'" % plan.refPhrase
            cursor.execute(query)
            if len(cursor.fetchall()) > 0:
                paramValue = plan.refPhrase
            else:
                # TODO  lookup the ref phrase using geocoding service and add it to the database
                pass
            db.close()
        # update plan graph
        if paramValue:
            plan.parent.values.append(paramValue)
            plan.parent.status = param_status_hasValue
            plan.mentalState.execStatus = exec_success
            plan.generatedValues.append(paramValue)
            for agent in plan.agents:
                for parent_agent in plan.parent.parent.agents:
                    if agent.id == parent_agent.id:
                        parent_agent.mentalState.execStatus = exec_paramReady
                        break
        else:
            plan.mentalState.execStatus = exec_failure

    def IdentifyAreaFromSpeech(self, plan):
        print "Execute: IdentifyAreaFromSpeech: %s" % plan.refPhrase
        paramValue = ""
        refPhrase = " ".join(plan.refPhrase.split("_"))
        # only support postgresql right now
        if self.datasource and self.datasource.get("type", "") == "postgresql":
            db = psycopg2.connect(self.dsn)
            cursor = db.cursor()
            query = "SELECT name FROM geo_contents where name = '%s'" % refPhrase
            cursor.execute(query)
            if len(cursor.fetchall()) > 0:
                paramValue = refPhrase
            else:
                # TODO  lookup the ref phrase using geocoding service and add it to the database
                pass
            db.close()
        # update plan graph
        if paramValue:
            plan.parent.values.append(paramValue)
            plan.parent.status = param_status_hasValue
            plan.mentalState.execStatus = exec_success
            plan.generatedValues.append(paramValue)
        else:
            plan.mentalState.execStatus = exec_failure
                
    def GenerateEPZs(self, plan):
        """docstring for GenerateEPZs"""
        plan.mentalState.execStatus = exec_failure
        if self.datasource and self.datasource.get("type", "") == "postgresql":
            db = psycopg2.connect(self.dsn)
            cursor = db.cursor()
            query = "SELECT name FROM geo_contents where name like '%epz'"
            cursor.execute(query)
            if len(cursor.fetchall()) > 0:
                paramLoc = plan.searchParamByName("ImpactedArea")
                paramLoc.status = param_status_hasValue
                for row in cursor:
                    if row[0]:
                        paramLoc.values.append(row[0])
                plan.mentalState.execStatus = exec_success
            else:
                # TODO  create the epzs using sql
                pass
            db.close()
    
    def GeneratePlumeModel(self, plan):
        """docstring for GenerateEPZs"""
        print "Execute: GeneratePlumeModel"
        plan.mentalState.execStatus = exec_failure
        if self.datasource and self.datasource.get("type", "") == "postgresql":
            db = psycopg2.connect(self.dsn)
            cursor = db.cursor()
            query = "SELECT name FROM geo_contents where name = 'plume model'"
            cursor.execute(query)
            results = cursor.fetchall()
            if len(results) > 0:
                for row in results:
                    if row[0]:
                        plan.generatedValues.append(row[0])
                plan.mentalState.execStatus = exec_success
            else:
                # TODO  create the plume model using sql
                pass
            db.close()


def main():
  pass
  
if __name__ == '__main__':
	main()