#!/usr/bin/python3

import sys

for line in sys.stdin:
	words = line.split()
	sorted_words = sorted(words)
	print(' '.join(sorted_words))
