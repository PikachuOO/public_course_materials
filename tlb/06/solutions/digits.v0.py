#!/usr/bin/python

import sys, re

for line in sys.stdin:
    line = re.sub(r'[0-4]', '<', line)
    line = re.sub(r'[6-9]', '>', line)
    sys.stdout.write(line)
# Note above line can also be (Python 3 only):
#   print(line, end='')
