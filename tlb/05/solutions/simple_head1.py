#!/usr/bin/python

import re, sys


n_lines = 10
if len(sys.argv) > 1 and re.match(r'-[0-9]+', sys.argv[1]):
    n_lines = int(sys.argv.pop(1)[1:])

# inefficient - reads entire file
sys.stdout.write("".join(sys.stdin.readlines()[0:n_lines]))
