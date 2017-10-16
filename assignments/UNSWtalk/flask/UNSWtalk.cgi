#!/usr/bin/python3

# This script allows game.py to also be run as a CGI script
#
# You should not need to change this script
#

import os, sys, traceback

try:
    from wsgiref.handlers import CGIHandler
    from werkzeug.debug import DebuggedApplication

    from UNSWtalk import app

    if 'PATH_INFO' not in os.environ:
        os.environ['PATH_INFO'] = ''

    # run the Flask app in debug mode
    app.secret_key = 'correct horse battery staple'
    app.debug = True
    CGIHandler().run(DebuggedApplication(app))
except Exception:
    # catch any exceptions that escape Flask and print useful information
    print('Content-Type: text/plain\n')
    etype, evalue, etraceback = sys.exc_info()
    print("\n".join(traceback.format_exception_only(etype, evalue)))
    traceback.print_exc()
