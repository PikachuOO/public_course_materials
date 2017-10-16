#!/usr/bin/python

import re, sys, fileinput

pattern = sys.argv.pop(1)
for line in fileinput.input():
    if re.search(pattern, line):
        sys.stdout.write(line)
