#!/usr/bin/python3
import re

for line in open("course_codes"):
    r = re.match('COMP(.*) Software (C.*)', line)
    if r:
        print(r.group(0))
        print(r.group(1))
