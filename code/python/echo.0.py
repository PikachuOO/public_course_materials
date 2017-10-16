#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# Python implementation of /bin/echo

# Note this prints an extra space on the end of the line

from __future__ import print_function  # Python 2.6+ compatibility

import sys

for arg in sys.argv[1:]:
    print(arg, end=' ')
print()
