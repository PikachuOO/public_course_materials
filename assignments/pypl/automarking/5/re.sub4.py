#!/usr/bin/python3
import sys, re
a = '1'
for i in range(8):
        a = re.sub("1", "11", a)
        print(len(a))
