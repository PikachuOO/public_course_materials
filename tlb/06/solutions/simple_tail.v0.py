#!/usr/bin/python

import sys,os

# inefficient for large files but simple
for filename in sys.argv[1:]:
    lines = open(filename).readlines()
    tail = lines[-10:]
    for line in tail:
        sys.stdout.write(line)
# Above line can also be in Python3:
#       print(line, end='')
