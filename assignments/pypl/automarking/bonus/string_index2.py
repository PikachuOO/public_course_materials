#!/usr/bin/python3
import sys

for i in sys.stdin.readlines():
    for j in range(int(sys.argv[1]), len(i)):
        sys.stdout.write(i[j])
