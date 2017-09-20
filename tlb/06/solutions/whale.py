#!/usr/bin/python

import re, sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage: %s <whale species>\n" % sys.argv[0])
    sys.exit(1)
target_species = sys.argv[1]

n_pods = 0
n_individuals = 0
for line in sys.stdin:
    m = re.search(r'(\d+)\s*(.+)$', line)
    if m:
        count = m.group(1)
        species = m.group(2)
        if species == target_species:
            n_pods += 1
            n_individuals += int(count)
print("%s observations: %d pods, %d individuals" % (target_species, n_pods, n_individuals))