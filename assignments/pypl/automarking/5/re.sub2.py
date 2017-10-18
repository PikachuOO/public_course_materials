#!/usr/bin/python3
import re
line = 'The quick brown fox jumped over the lazy dog'
pattern = r'[aeiou]'
replacement = 'y'
line2 = re.sub(pattern, replacement, line)
print(line2)
