#!/usr/bin/python
import sys, glob, re, collections, math

frequency = {}
n_words = collections.defaultdict(int)
for file in glob.glob("lyrics/*"):
    artist = re.sub(r'.*/', '', file)
    artist = re.sub(r'.txt$', '', artist)
    artist = re.sub(r'_', ' ', artist)
    frequency[artist] = collections.defaultdict(int)
    for line in open(file):
        line = line.lower()
        for word in re.findall(r'[a-z]+', line, re.I):
            frequency[artist][word] += 1
            n_words[artist] += 1

for word in sys.argv[1:]:
    word = word.lower()
    for artist in sorted(frequency.keys()):
        f = frequency[artist][word]
        n = n_words[artist]
        print("log((%d+1)/%6d) = %8.4f %s" % (f, n, math.log((f+1)/float(n)), artist))
