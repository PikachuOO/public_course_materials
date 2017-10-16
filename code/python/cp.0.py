#!/usr/bin/python
# Written by andrewt@cse.unsw.edu.au  for COMP2041
# Simple cp implementation using line by line I/O

import sys,os
if len(sys.argv) != 3:
    sys.stderr.write("Usage: %s <infile> <outfile>\n" % sys.argv[0])
    # or (Python3 only):
    # print("Usage:",  sys.argv[0], "<infile> <outfile>", file=sys.stderr)
    sys.exit(1)
outfile = open(sys.argv[2], 'w')
for line in open(sys.argv[1]):
    outfile.write(line)