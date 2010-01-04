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
  
  url = "http://127.0.0.1:8080/dialogues/"
  data = {
    "id" : "test123",
    "participants" : [{"name": "Jim", "id":"jim@abc.com"}]
  }
  #print urllib.urlencode(str(json.dumps(data)))
  f = urllib2.urlopen(url, json.dumps(data))
  data = f.read()
  print "new dialogue:"
  print data
  f.close()
  
  # 2. add a new participant
  url = "http://127.0.0.1:8080/dialogues/test123/participants/"
  data = {"name": "Jill", "id":"jill@abc.com"}
  f = urllib2.urlopen(url, json.dumps(data))
  data = f.read()
  print "add new participant:"
  print data
  f.close()
  
  # 3. add a new message
  url = "http://127.0.0.1:8080/dialogues/test123/messages/"
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
  
  # 4. Get the current planGraph
  url = "http://127.0.0.1:8080/dialogues/test123/plangraph/"
  f = urllib2.urlopen(url)
  data = f.read()
  print "the current plangraph:"
  print data
  f.close()

  # 5. Get the first map response
  url = "http://127.0.0.1:8080/dialogues/test123/responses/%s" % responderId
  f = urllib2.urlopen(url)
  data = f.read()
  print "the current map:"
  print data
  f.close()
  
if __name__ == '__main__':
  main()

