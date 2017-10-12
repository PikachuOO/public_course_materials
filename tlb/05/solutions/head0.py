#!/usr/bin/python

import re, sys, itertools

n_lines = 10

if len(sys.argv) > 1 and re.match(r'-[0-9]+', sys.argv[1]):
    n_lines = int(sys.argv.pop(1)[1:])

if len(sys.argv) == 1:
    sys.argv.append("-")

for filename in sys.argv[1:]:
    try:
        print("==> %s <==" % filename)
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)
        for line in itertools.islice(stream, n_lines):
            sys.stdout.write(line)
        if filename != "-":
            stream.close()
    except IOError as  e:
        (errno, strerror) = e.args
        print("%s: can not open: %s" % (filename, strerror))
