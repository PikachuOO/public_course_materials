#!/usr/bin/python3
import re
line = 'The quick brown fox jumped over the lazy dog'
m = re.search('quick(.*)brown', line)
print(m.group(0))
print(m.group(1))
