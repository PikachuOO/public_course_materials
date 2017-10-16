#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# compute Pythagoras' Theorem
# Works with Python 3.3+

import math, sys

print("Enter x: ", end='', flush=True)
x = float(sys.stdin.readline())
print("Enter y: ", end='', flush=True)
y = float(sys.stdin.readline())
pythagoras = math.sqrt(x * x + y * y)
print("The square root of %f squared + %f squared is %f" % (x, y, pythagoras))
