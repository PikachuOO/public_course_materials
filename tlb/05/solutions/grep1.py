#!/usr/bin/python

import re, sys, fileinput

pattern = re.compile(sys.argv.pop(1))
sys.stdout.write("".join(filter(pattern.search, fileinput.input())))

