#!/usr/bin/python

import re, sys

current_count = 0
current_species = ""
for line in sys.stdin:
    m = re.search(r'(\d+)\s*(.+)$', line)
    if m:
        count = int(m.group(1))
        species = m.group(2)
        if species  == current_species:
            current_count += count
        else:
            if current_count:
                print(current_count + " " +current_species)
            current_count = count
            current_species = species
    else:
        print("Sorry couldn't parse: %s" % line)

if current_count:
    print(current_count + " " +current_species)
