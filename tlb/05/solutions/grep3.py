#!/usr/bin/python

import re, sys, fileinput

if sys.argv[1] == "-v":
    sys.argv.pop(1)
    p = re.compile(sys.argv.pop(1))
    f = lambda x: not p.search(x)
else:
    f = re.compile(sys.argv.pop(1))
sys.stdout.write(filter(f, fileinput.input()))

