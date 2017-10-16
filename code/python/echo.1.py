#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# Python implementation of /bin/echo
# Clumsy but works with any Python version

import sys

if len(sys.argv) > 1:
    sys.stdout.write(sys.argv[1])
for arg in sys.argv[2:]:
    sys.stdout.write(' ' + arg)
print()
