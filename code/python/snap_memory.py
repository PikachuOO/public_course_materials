#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# Reads lines of input until end-of-input
# Print snap! if a line has been seen previously

import sys
seen = {}
while 1:
    sys.stdout.write("Enter line: ")
    sys.stdout.flush()
    line = sys.stdin.readline()
    if not line:
        break
    if line in seen:
        print("Snap!")
    seen[line] = 1
