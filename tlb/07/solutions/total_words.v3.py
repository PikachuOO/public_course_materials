#!/usr/bin/python

import sys, re

lines = "".join(l for l in sys.stdin).lower()
words = re.findall(r'[a-z]+', lines, flags=re.I)
print("%d words" % len(words))
