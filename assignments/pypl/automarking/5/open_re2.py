#!/usr/bin/python3
import re

for line in open("course_codes"):
    if re.search('Cons.*tion', line) and re.match('COMP2', line):
        print(line, end='')
