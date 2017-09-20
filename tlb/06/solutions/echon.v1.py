#!/usr/bin/python

import re, sys

if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <number of lines> <string>\n" % sys.argv[0])
# Above line can also be in Python3
#   print("Usage: %s <number of lines> <string>" % sys.argv[0], file=sys.stderr)
    sys.exit(1)

if not re.match(r'^\d+$', sys.argv[1]):
    sys.stderr.write("%s: argument 1 must be a non-negative integer\n" % sys.argv[0])
    sys.exit(1)

for i in range(int(sys.argv[1])):
    print(sys.argv[2])
