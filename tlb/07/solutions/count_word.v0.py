#!/usr/bin/python

import re, sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage %s: <word>\n" % sys.argv[0])
    sys.exit(1)

specified_word = sys.argv[1].lower()

count = 0
for line in sys.stdin:
    line = line.lower()
    words = re.split(r'[^a-z]+', line)
    for word in words:
        if word == specified_word:
            count += 1

print("%s occurred %d times" % (specified_word, count))
