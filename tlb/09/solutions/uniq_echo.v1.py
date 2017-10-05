#!/usr/bin/python3

import sys

seen = {}
for argument in sys.argv[1:]:
	if argument not in seen:
		print(argument, end=' ')
		seen[argument] = 1
print()
