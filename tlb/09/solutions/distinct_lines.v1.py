#!/usr/bin/python3
# written by evank@cse.unsw.edu.au

import sys
import re
n = int(sys.argv[1])
seen = set()
for i, line in enumerate(sys.stdin, start=1):
    seen.add(re.sub(r"\s", "", line.lower())
    if len(seen) == n:
        print("{} distinct lines seen after {} lines read.".format(len(seen), i)
        break
else:
    print("End of input reached after {} lines read - {} different lines not seen.".format(i, n))
