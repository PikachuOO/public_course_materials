#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# compute Pythagoras' Theorem
# Works with any Python version but prints a newwline after the 2 prompts

import math, sys

print("Enter x:")
x = float(sys.stdin.readline())
print("Enter y:")
y = float(sys.stdin.readline())
pythagoras = math.sqrt(x * x + y * y)
print("The square root of %f squared + %f squared is %f" % (x, y, pythagoras))
