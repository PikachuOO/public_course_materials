#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au for COMP2041
# count lines of C source code
import glob
total = 0
for filename in glob.glob("*.[ch]"):
    with open(filename) as f:
        lines = f.readlines()
        n_lines = len(lines)
        print("%7d %s" % (n_lines, filename))
        total += n_lines
print("%7d total"%total)
