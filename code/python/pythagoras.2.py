#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# compute Pythagoras' Theorem
# Works with any Python version

import math, sys

sys.stdout.write("Enter x: ")
sys.stdout.flush()
x = float(sys.stdin.readline())
sys.stdout.write("Enter x: ")
sys.stdout.flush()
y = float(sys.stdin.readline())
pythagoras = math.sqrt(x * x + y * y)
print("The square root of %f squared + %f squared is %f" % (x, y, pythagoras))
