#!/usr/bin/python3
import re

for line in open("poem"):
    if re.search('Ozymandias', line):
        print(line, end='')
