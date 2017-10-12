#!/usr/bin/python

import re, sys

n_lines = 10

if len(sys.argv) > 1 and re.match(r'-[0-9]+', sys.argv[1]):
    arg = sys.argv[1]
    arg = arg[1:] # remove first character
    n_lines = int(arg)

n = 1
for line in sys.stdin:
    if n > n_lines:
        break
    sys.stdout.write(line)
    n += 1
