#!/usr/bin/python3
import re, sys
n = [(max([float(x) for x in re.findall(r'(\-?\d+(?:\.\d+)?)', line) if x]),line) for line in sys.stdin]
print ''.join([line for (x,line) in n if x == sorted(n)[0][0]]),
