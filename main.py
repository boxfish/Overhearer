#!/usr/bin/env python
# encoding: utf-8
"""
main.py

Created by Bo Yu on 2009-12-14.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import web
import json
import yaml
from DMLib.DialogueManager import DialogueManager

urls = (
  "/dialogues/(.+)/map/?", "MapHandler",
  "/dialogues/(.+)/plangraph/?", "PlanGraphHandler",
  "/dialogues/(.+)/participants/(.+)/?", "ParticipantHandler",
  "/dialogues/(.+)/participants/?", "ParticipantsHandler",
  "/dialogues/(.+)/messages/(.+)/?", "MessageHandler",
  "/dialogues/(.+)/messages/?", "MessagesHandler",
  "/dialogues/(.+)/?", "DialogueHandler",
  "/dialogues/?", "DialoguesHandler",
  "", "Redirect",
  "/(.*)", "IndexHandler"
)

# maintain the list of ongoing dialogues
dialogues = []

config = None

def getDialogueById(dialogueId):
  """docstring for __getDialogueById"""
  if dialogueId:
    for dialogue in dialogues:
      if dialogue.id == dialogueId:
        return dialogue
  return None

class MapHandler:        
  def GET(self, dialogueId):
    dialogue = getDialogueById(dialogueId)
    if dialogue:
      web.header('Content-Type', 'text/xml')
      return dialogue.getMapXML()
    else:
      response = {}
      response["status"] = "error"
      response["message"] = "the dialogue (%d) does not exists!" % dialogueId
      return json.dumps(response)

class PlanGraphHandler:        
  def GET(self, dialogueId):
    dialogue = getDialogueById(dialogueId)
    if dialogue:
      web.header('Content-Type', 'text/xml')
      return dialogue.getPlanGraphXML()
    else:
      response = {}
      response["status"] = "error"
      response["message"] = "the dialogue (%d) does not exists!" % dialogueId
      return json.dumps(response)
      
    
class ParticipantHandler:        
  def GET(self, name, name2):
    if not name: 
      name = 'rest'
    return 'ParticipantHandler: ' + name + name2 + '!'

class ParticipantsHandler:        
  def GET(self, name):
    if not name: 
      name = 'rest'
    return 'ParticipantsHandler: ' + name + '!'
  def POST(self, dialogueId):
    response = {}
    dialogue = getDialogueById(dialogueId)
    if dialogue:
      data = json.loads(web.data())
      if data and data.has_key("id"):
        dialogue.addParticipant(data)
        response["status"] = "success"
        response["participant"] = {
          "id" : data["id"]
        }
      else:
        response["status"] = "error"
        response["message"] = "the participant id must be specified!"
    else: 
      response["status"] = "error"
      response["message"] = "the dialogue (%d) does not exists!" % dialogueId
    return json.dumps(response)  
    
class MessageHandler:        
  def GET(self, name, name2):
    if not name: 
      name = 'rest'
    return 'MessageHandler: ' + name + '!'

class MessagesHandler:        
  def GET(self, name):
    if not name: 
      name = 'rest'
    return 'MessagesHandler: ' + name + '!'
  def POST(self, dialogueId):
    response = {}
    dialogue = getDialogueById(dialogueId)
    if dialogue:
      data = json.loads(web.data())
      if data and data.has_key("speakerId") and data.has_key("message"):
        response = dialogue.process(data)
      else:
        response["status"] = "error"
        response["message"] = "the message cannot be processed!"
    else: 
      response["status"] = "error"
      response["message"] = "the dialogue (%s) does not exists!" % dialogueId
    response["dialogueId"] = dialogueId
    return json.dumps(response)  
  
            
class DialogueHandler:        
  def GET(self, name):
    if not name: 
      name = 'rest'
    return 'DialogueHandler: ' + name + '!'

class DialoguesHandler:        
  def GET(self):
    return 'DialoguesHandler: ' + '!'
  def POST(self):
    # initiate a new dialogue
    response = {}
    data = json.loads(web.data())
    id = ""
    if data.has_key("id"):
      id = data["id"]
      for dialogue in dialogues:
        if dialogue.id == id:
          response["status"] = "error"
          response["message"] = "the dialogue already exists!"
          return json.dumps(response)
    if data.has_key("participants") and len(data["participants"]) > 0:
      f = open('config.yaml')
      config = yaml.load(f)
      f.close()
      if config:
        dialogue = DialogueManager(config, id)
        for participant in data["participants"]:
          dialogue.addParticipant(participant)
        dialogues.append(dialogue)
        response["status"] = "success"
        response["dialogueId"] = id
      else:
        response["status"] = "error"
        response["message"] = "no config file is found!"  
    else:
      response["status"] = "error"
      response["message"] = "the dialogue must involves at least one participant!"
    return json.dumps(response)

class Redirect:
  def GET(self):
    raise web.seeother('/')
    
class IndexHandler:        
  def GET(self, data):
    return web.template.render('templates').index()

app = web.application(urls, locals())

if __name__ == '__main__':
  app.run()