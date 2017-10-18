#!/usr/bin/python3
import fileinput
i = 0
for line in fileinput.input():
    i = i + 1
print(i)
