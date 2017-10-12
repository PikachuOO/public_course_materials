#!/usr/bin/python

import sys, re

word = sys.argv[1].lower()
lines = "".join(l for l in sys.stdin).lower()
words = re.findall(r'[a-z]+', lines, flags=re.I)
print("%s occurred %d times" % (word, words.count(word)))
