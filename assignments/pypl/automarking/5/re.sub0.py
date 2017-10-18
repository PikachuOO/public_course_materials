#!/usr/bin/python3
import re
line = 'The quick brown fox jumped over the lazy dog'
line2 = re.sub (r'[aeiou]', '', line)
print(line2)
