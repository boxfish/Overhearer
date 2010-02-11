#!/usr/bin/env python
# encoding: utf-8
"""
Knowledge Base for postgresql

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os
import psycopg2

from PlanGraph import *

class KBasePostgresql():
    """knowledge base"""
    def __init__(self, dsn):
        # dsn: data source name built from keywords (dbname, host, port, user, password)
        # e.g. : "dbname=test user=test"
        self.dsn = dsn
        
    def parsePhrases(self, phrases):
        """parsePhrases"""
        tempPlans = []
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        for phrase in phrases:
            query = "SELECT PID, Phrase, Type, Phrases.ActionName, Alias, ActType, Complexity, RefID FROM Phrases, Actions where Phrases.ActionName = Actions.ActionName and Phrase='%s'" % phrase
            print query
            cursor.execute(query)
            for row in cursor:
                planNode = PlanNode()
                planNode.phrase = str(row[1])
                planNode.actionName = str(row[3])
                planNode.alias = str(row[4])
                planNode.actionType = str(row[5]).upper()
                planNode.complexity = str(row[6]).lower()
                if planNode.actionType == "ID_PARA":
                    planNode.refType = str(row[2]).split("-")[1]
                    planNode.refPhrase = str(row[1])
                    planNode.refId = int(row[7])
                else:
                    planNode.refType = ""
                tempPlans.append(planNode)
        db.close()
        return tempPlans
    
    def selectActionsByPhrase(self, phrase):
        """SelectActionsByPhrase"""
        query = "SELECT PID, Phrase, Type, Phrases.ActionName, Alias, ActType, Complexity, RefID FROM Phrases, Actions where Phrases.ActionName = Actions.ActionName and Phrase='%s'" % phrase
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        cursor.execute(query)
        db.close()
        return cursor.fetchall()
    
    def hasRecipe(self, actionName):
        """docstring for hasRecipe"""
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        query = "SELECT ActionName FROM Actions where ActionName = '%s'" % actionName
        cursor.execute(query)
        if len(cursor.fetchall()) > 0:
            db.close()
            return True
        else: 
            db.close()
            return False
    
    def selectRecipe(self, actionName):
        """docstring for selectRecipe"""
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        query = "SELECT Action_no, ActionName, ActType, Recipe FROM Actions where ActionName = '%s'" % actionName
        cursor.execute(query)
        for row in cursor:
            if row[3]:
                db.close()
                return row[3]
        db.close()
        return ""
        
    def getGeoContentType(self, name):
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        query = "SELECT type FROM geo_contents where name = '%s'" % name
        cursor.execute(query)
        for row in cursor:
            if row[0]:
                db.close()
                return row[0]
        db.close()
        return ""
        
    def getGeoContentStyle(self, name):
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        query = "SELECT style FROM geo_contents where name = '%s'" % name
        cursor.execute(query)
        for row in cursor:
            if row[0]:
                db.close()
                return row[0]
        db.close()
        return ""

    def getGeoContentCenter(self, name):
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        query = "SELECT ST_X(ST_Centroid(geom)), ST_Y(ST_Centroid(geom)) FROM geo_contents where name = '%s'" % name
        cursor.execute(query)
        for row in cursor:
            if row[0] and row[1]:
                db.close()
                return (row[0], row[1])
        db.close()
        return None
        
    def getActionContext(self, actionName):
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        query = "SELECT geo_content_name FROM action_geo_content where action_name = '%s' order by render_order" % actionName
        print query
        cursor.execute(query)
        contents = []
        for row in cursor:
            if row[0]:
                contents.append(row[0])
        db.close()
        return contents
    
    def getOrderedFeatures(self, feature_names):
        """docstring for getOrderedFeatures"""
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        query = "SELECT name FROM geo_contents where name in (%s) order by render_order" % ", ".join(["'%s'" % k for k in feature_names])
        print query
        cursor.execute(query)
        contents = []
        for row in cursor:
            if row[0]:
                contents.append(row[0])
        db.close()
        return contents
    
                
    def getBbox(self, feature_names):
        """docstring for getOrderedFeatures"""
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        query = "SELECT ST_XMin(ST_Extent(geom)), ST_YMin(ST_Extent(geom)),ST_XMax(ST_Extent(geom)),ST_YMax(ST_Extent(geom)) FROM geo_contents where name in (%s)" % ", ".join(["'%s'" % k for k in feature_names])
        print query
        cursor.execute(query)
        bbox = []
        bbox.extend(cursor.fetchone())
        db.close()
        return bbox
    
    def executeSQL(self, query):
        """docstring for executeSQL"""
        db = psycopg2.connect(self.dsn)
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()
        return result
        
def main():
    pass
    
if __name__ == '__main__':
    main()
