#!/usr/bin/python
import fileinput, re
for line in fileinput.input():
    sys.out.write(re.sub(r'[aeiou]', '', line, flags=re.I))
