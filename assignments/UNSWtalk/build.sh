#!/bin/sh
unset CDPATH
rm -f flask.zip
cd flask
chmod 700 *
zip -qr ../flask.zip UNSWtalk.cgi UNSWtalk.py static templates
chmod 644 ../flask.zip
