#!/usr/bin/env python
# encoding: utf-8
"""
Knowledge Base for sqlite

Created by Bo Yu on 2009-12-11.
"""
__author__ = 'byu@ist.psu.edu (Bo Yu)'

import sys
import os
#from pysqlite2 import dbapi2 as sqlite
import sqlite3

from PlanGraph import *

class KBaseSqlite():
  """knowledge base"""
  def __init__(self, dbFile):
    self.dbFile = dbFile
    
  def parsePhrases(self, phrases):
    """parsePhrases"""
    tempPlans = []
    db = sqlite3.connect(self.dbFile)
    cursor = db.cursor()
    for phrase in phrases:
      query = "SELECT PID, Phrase, Type, Phrases.ActionName, Alias, ActType, Complexity, RefID FROM Phrases, Actions where Phrases.ActionName = Actions.ActionName and Phrase='%s'" % phrase
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
    db = sqlite3.connect(self.dbFile)
    cursor = db.cursor()
    cursor.execute(query)
    db.close()
    return cursor.fetchall()
  
  def hasRecipe(self, actionName):
    """docstring for hasRecipe"""
    db = sqlite3.connect(self.dbFile)
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
    db = sqlite3.connect(self.dbFile)
    cursor = db.cursor()
    query = "SELECT Action_no, ActionName, ActType, Recipe FROM Actions where ActionName = '%s'" % actionName
    cursor.execute(query)
    for row in cursor:
      if row[3]:
        db.close()
        return row[3]
    db.close()
    return ""
    
  def executeSQL(self, query):
    """docstring for executeSQL"""
    db = sqlite3.connect(self.dbFile)
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result
    
def main():
  phrases = ["evacuation"]
  kb = KBaseSqlite("kboop.sqlite")
  print kb.parsePhrases(phrases)
  
  pass
  
if __name__ == '__main__':
	main()