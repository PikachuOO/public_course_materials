#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# sum integers supplied as command line arguments
# no check that arguments are integers

import sys

sum = 0
for arg in sys.argv[1:]:
    sum += int(arg)
print("Sum of the numbers is %s" % sum)

