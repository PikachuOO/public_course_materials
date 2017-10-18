#!/usr/bin/python3
a = 1
b = 10
while b:
    a = a << 1
    b = b - 1
a = a ^ a
if not a:
    print("yay!")

