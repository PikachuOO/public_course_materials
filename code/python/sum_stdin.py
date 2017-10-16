#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# count how many people enrolled in each course
# Read numbers until end of input (or a non-number)  is reached
# then print the sum of the numbers

import re, sys

sum = 0

while 1:
    line = sys.stdin.readline()
    line = line.strip() # remove leading & trailing white space
    # Test if string looks like an integer or real (scientific notation not handled!)
    if not re.search(r'^\d[.\d]*$', line):
        break
    sum += float(line)

print("Sum of the numbers is %s" % sum)
