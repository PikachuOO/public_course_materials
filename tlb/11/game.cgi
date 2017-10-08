#!/usr/bin/python3

# This script allows game.py to also be run as a CGI script

import os, sys
from wsgiref.handlers import CGIHandler
os.chdir('../../../private/tlb/11/solutions/')
sys.path.append('.')
from game import app
app.secret_key = 'correct horse battery staple'
CGIHandler().run(app)
