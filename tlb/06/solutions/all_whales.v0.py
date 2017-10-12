#!/usr/bin/python

import re, sys

n_pods = {}
n_individuals = {}
for line in sys.stdin:
    line = line.lower()              # convert line to lower case
    line = line.strip()              # remove surrounding white space
    line = re.sub(r's?$', '', line)  # change to singular
    line = re.sub(r'\s+', ' ', line) # convert sequential white-space charcaters to a single space
    m = re.search(r'(\d+)\s*(.*)$', line)
    if m:
        count = int(m.group(1))
        species = m.group(2)
        if species in n_pods:
            n_pods[species] += 1
            n_individuals[species] += count
        else:
            n_pods[species] = 1
            n_individuals[species] = count
    else:
        print("Sorry couldn't parse: %s" % line)

for species in sorted(n_pods):
    print("%s observations: %d pods, %d individuals" % (species, n_pods[species], n_individuals[species]))
