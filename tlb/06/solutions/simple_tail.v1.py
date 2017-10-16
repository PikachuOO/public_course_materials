#!/usr/bin/python

import sys,os

# inefficient for large files but simple
for filename in sys.argv[1:]:
    sys.stdout.write("".join(open(filename).readlines()[-10:]))
