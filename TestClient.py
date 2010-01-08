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

def main():
    # 1. initiate new dialogue 
    base_url = "http://127.0.0.1:8080/"
    url = base_url + "dialogues/"
    data = {
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
    message = {"speakerId":"jill@abc.com", "message":"There is a nuclear release and we need to plan evacuation"}
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
    
if __name__ == '__main__':
  main()

