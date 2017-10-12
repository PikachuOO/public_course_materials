#!/usr/bin/python

import sys

if len(sys.argv) != 4:
    sys.stderr.write("Usage: %s <n> <m> <file>\n" % sys.argv[0])
    sys.exit(1)

for line in open(sys.argv[3]):
    line = line.rstrip('\n')
    print(line[int(sys.argv[1])-1:int(sys.argv[2])])
