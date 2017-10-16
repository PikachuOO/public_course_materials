#!/usr/bin/python

import re, sys, itertools

n_lines = 10
if len(sys.argv) > 1 and re.match(r'-[0-9]+', sys.argv[1]):
    n_lines = int(sys.argv.pop(1)[1:])

for line in itertools.islice(sys.stdin, n_lines):
    sys.stdout.write(line)
