#!/usr/bin/python

import re, sys

count = 0
for line in sys.stdin:
    for word in re.findall(r'[a-z]+', line, re.I):
        count += 1

print("%d words" % count)
