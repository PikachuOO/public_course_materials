#!/usr/bin/python3
import re

for line in open("poem"):
    if re.match('and', line):
        print(line,, end='')
