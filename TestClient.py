#!/usr/bin/env python
# encoding: utf-8
"""
TestClient.py

Created by Bo Yu on 2009-12-15.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import urllib, urllib2
import json

def TestDialogues():
    # 1. initiate new dialogue 
    base_url = "http://127.0.0.1:8080/"
    url = base_url + "dialogues/"
    data = {
        "id" : "testforevacuation",
        "participants" : [{"name": "Jim", "id":"jim@abc.com"}]
    }
    f = urllib2.urlopen(url, json.dumps(data))
    data = f.read()
    print "new dialogue:"
    print data
    f.close()
    dlgId = json.loads(data).get("dialogueId")
    
    # 2. get the dialogue list
    url = base_url + "dialogues/"
    f = urllib2.urlopen(url)
    data = f.read()
    print "curr dialogues:"
    print data
    f.close()
    
    # 3. add a new participant
    
    url = base_url + "dialogues/%s/participants/" % dlgId
    data = {"name": "Jill", "id":"jill@abc.com"}
    f = urllib2.urlopen(url, json.dumps(data))
    data = f.read()
    print "add new participant:"
    print data
    f.close()
    
    # 4. add a new message
    
    url = base_url + "dialogues/%s/messages/" % dlgId
    message = {"speakerId":"jill@abc.com", "message":"There is a nuclear release at the Three Mile Island Nuclear Station and we need to plan response actions"}
    f = urllib2.urlopen(url, json.dumps(message))
    data = f.read()
    print "add new message: %s" % message["message"]
    print data
    f.close()
    responderId = "-1"
    data = json.loads(data)
    if type(data) == list:
        for response in data:
            if response["type"] == "map":
                # get the first map response
                print "ID:" + response["id"]
                responderId = response["id"]
                break
    
    '''    
    # 5. Get the current planGraph
    url = base_url + "dialogues/%s/plangraph/" % dlgId
    f = urllib2.urlopen(url)
    data = f.read()
    print "the current plangraph:"
    print data
    f.close()

    
    # 6. Get the first map response
    url = base_url + "dialogues/%s/responses/%s/" % (dlgId, responderId)
    f = urllib2.urlopen(url)
    data = f.read()
    print "the current map:"
    print data
    f.close()
    '''
    
def TestMaps():
    # 1. post a new static map 
    base_url = "http://127.0.0.1:8080/"
    url = base_url + "maps/dialogueId/respId/timestamp/static.png"
    url = "http://127.0.0.1:8080/maps/d7bbe341-b93f-485b-8607-05b1ea0412de/0/2010-01-08-15-32-03/static.png"
    data = {
        "width" : 800,
        "height" : 800,
        "minx" : -179.0,
        "miny" : -89.0,
        "maxx" : 179.0,
        "maxy" : 89.0
    }
    f = urllib2.urlopen(url, json.dumps(data))
    #data = f.read()
    print "post static map:"
    f.close()

def TestDialogues2():
    """docstring for TestDialogues2"""
    base_url = "http://127.0.0.1:8080/"
    dlgId = "testforpickled15"
    url = base_url + "dialogues/%s/messages/" % dlgId
    message = {"speakerId":"jill@abc.com", "message":"It is at the Crystal River Nuclear Power plant"}
    f = urllib2.urlopen(url, json.dumps(message))
    data = f.read()
    print "add new message: %s" % message["message"]
    print data
    f.close()
    responderId = "-1"
    data = json.loads(data)
    if type(data) == list:
        for response in data:
            if response["type"] == "map":
                # get the first map response
                print "ID:" + response["id"]
                responderId = response["id"]
                break
        
if __name__ == '__main__':
  #TestMaps()
  TestDialogues()
