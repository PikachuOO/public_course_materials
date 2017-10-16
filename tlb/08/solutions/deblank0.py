#!/usr/bin/python
# delete blank lines from specified files
# simple code which could lose data, if a write error occurs
import sys, re

for filename in sys.argv[1:]:
    with open(filename) as f:
        lines = f.readlines()
    with open(filename,'w') as f:
        for line in lines:
            if not re.match(r'^\s*$', line):
                f.write(line)
