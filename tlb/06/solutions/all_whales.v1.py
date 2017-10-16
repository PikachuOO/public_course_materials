#!/usr/bin/python

import re, sys, collections

n_pods = collections.Counter()
n_individuals = collections.Counter()
for line in sys.stdin:
    line = line.lower()              # convert line to lower case
    line = line.strip()              # remove surrounding white space
    if line.endswith('s'):           # remove trailing s pythonically
        line = line[:-1]
    line = re.sub(r'\s+', ' ', line) # convert sequential white-space charcaters to a single space
    count, species = line.split(' ', 1)  # split at most once (ie. into 2 parts)
    n_pods[species] += 1
    n_individuals[species] += int(count)

for species in sorted(n_pods):
    print("%s observations: %d pods, %d individuals" % (species, n_pods[species], n_individuals[species]))
