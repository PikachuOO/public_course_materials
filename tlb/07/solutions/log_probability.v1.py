#!/usr/bin/python

import sys, glob, re, collections, os, math

frequency = {}
n_words = {}
for f in glob.glob("lyrics/*.txt"):
    # remove directory, extension, and fix the underscores
    artist = os.path.splitext(os.path.basename(f))[0].replace('_', ' ')
    lines = open(f).read().lower()
    words = re.findall(r'[a-z]+', lines, flags=re.I)
    frequency[artist] = collections.Counter(words)
    n_words[artist] = len(words)

for word in sys.argv[1:]:
    for artist in sorted(frequency):
        f = frequency[artist][word.lower()]
        n = n_words[artist]
        print("log((%d+1)/%6d) = %8.4f %s" % (f, n, math.log(float(f + 1) / n), artist))
