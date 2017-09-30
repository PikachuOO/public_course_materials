#!/usr/bin/python

import sys, glob, re, collections, os

frequency = {}
n_words = collections.Counter()
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
        print("%4d/%6d = %.9f %s" % (f, n, float(f) / n, artist))
