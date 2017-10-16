#!/usr/bin/python
# Written by andrewt@cse.unsw.edu.au  for COMP2041
# Simple cp implementation using line by line I/O

import sys,os
if len(sys.argv) != 3:
    sys.stdout.write("Usage: %s <infile> <outfile>\n" % sys.argv[0])
    sys.exit(1)
open(sys.argv[2], 'w').writelines(open(sys.argv[1]))
