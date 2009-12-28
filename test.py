#!/usr/bin/env python
# encoding: utf-8
"""
test.py

Created by Bo Yu on 2009-12-14.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import web

import api

urls = (
  '/api', api.app_api,
  '/(.*)', 'index'
)
app = web.application(urls, locals())

class index:        
  def GET(self, name):
    if not name: 
      name = 'world'
    return 'Hello, ' + name + '!'

if __name__ == "__main__":
  app.run()