#!/usr/bin/python3
import fileinput

a = ''.join(fileinput.input())
b = []

for i in range(len(a)):
    b.append(a[i])

b = sorted(b)

print(''.join(b))
