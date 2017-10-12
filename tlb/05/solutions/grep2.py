#!/usr/bin/python

import re, sys, fileinput

do_opposite = 0

if sys.argv[1] == "-v":
    do_opposite = 1;
    sys.argv.pop(1)

pattern = sys.argv.pop(1)

for line in fileinput.input():
    if re.search(pattern, line):
        if not do_opposite:
            sys.stdout.write(line)
    else:
        if do_opposite:
            sys.stdout.write(line)
