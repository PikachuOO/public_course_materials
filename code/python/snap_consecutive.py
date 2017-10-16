#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# Reads lines of input until end-of-input
# Print snap! if two consecutive lines are identical

import sys
sys.stdout.write("Enter line: ")
sys.stdout.flush()
last_line = sys.stdin.readline()
while 1:
    sys.stdout.write("Enter line: ")
    sys.stdout.flush()
    line = sys.stdin.readline()
    if not line:
        break
    if line == last_line:
        print("Snap!")
    last_line = line
