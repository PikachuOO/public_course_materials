#!/usr/bin/python

import sys

if len(sys.argv) == 1:
    for line in reversed(list(sys.stdin)):
        sys.stdout.write(line)
else:
    for filename in sys.argv[1:]:
        with open(filename) as f:
            for line in reversed(list(f)):
                sys.stdout.write(line)
