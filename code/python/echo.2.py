#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# Python implementation of /bin/echo

from __future__ import print_function # Python 2.6+ compatibility

import sys

if len(sys.argv) > 1:
    print(argv[1], end='')
for arg in sys.argv[2:]:
    print(' ' + arg, end='')
print()
