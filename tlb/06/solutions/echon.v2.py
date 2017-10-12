#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <number of lines> <string>\n" % sys.argv[0])
    sys.exit(1)

# check argument is a positive int  (not required by exercise)
try:
    n = int(sys.argv[1])
except ValueError:
    n = -1
if n < 0:
    sys.stderr.write("%s: argument 1 must be a non-negative integer\n" % sys.argv[0])
    sys.exit(1)

sys.stdout.write((sys.argv[2] + "\n") * n)
