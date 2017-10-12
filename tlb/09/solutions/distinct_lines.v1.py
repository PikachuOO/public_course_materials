#!/usr/bin/python3

import re, sys

n_distinct_lines_needed = int(sys.argv[1])

n_lines = 0
lines_seen = {}
while 1:
	line = sys.stdin.readline()
	if not line:
		print("End of input reached after", n_lines, 'lines read - ', n_distinct_lines_needed, 'different lines not seen.')
		sys.exit(0)
	n_lines += 1
	line = line.lower()
	line = re.sub(r'\s', '', line)
	lines_seen[line] = 1
	if len(lines_seen.keys()) >= n_distinct_lines_needed:
		print(n_distinct_lines_needed, 'distinct lines seen after', n_lines, 'lines read.')
		sys.exit(0)

