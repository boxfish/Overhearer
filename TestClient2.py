#!/usr/bin/env python
# encoding: utf-8
"""
TestClient.py

Created by Bo Yu on 2009-12-12.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from DMLib.DialogueManager import DialogueManager

def main():
  dlgManager = DialogueManager()
  step = 0
  while 1:
    step = step + 1
    input = raw_input("Step %d: " % step)
    input = input.split(":")
    if input[0].lower() == "quit":
      break
    #request = Request(input[0], input[1])
    request = {}
    request["speakerId"] = input[0]
    request["message"] = input[1]
    print dlgManager.process(request)

if __name__ == '__main__':
  main()

