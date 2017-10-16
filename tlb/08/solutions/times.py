#!/usr/bin/python
import glob, sys, re

if len(sys.argv) != 4:
    sys.stdout.write("Usage: %s <n> <m> <column-width>\n\n" % sys.argv[0])
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])
width = int(sys.argv[3])
format = "%%%dd" % width

for x in range(1, n + 1):
    print(format % x)
    for y in range(1, m + 1):
        sys.stdout.write(' ' + (format % (x * y)))
    print()

