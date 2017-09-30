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

artists = list(frequency.keys())
debug = 0
for file in sys.argv[1:]:
    if file == '-d':
        debug = 1
        continue
    log_probability = collections.defaultdict(float)
    for line in open(file):
        line = line.lower()
        for word in re.findall(r'[a-z]+', line, re.I):
            for artist in artists:
                log_probability[artist] += math.log(((frequency[artist][word] + 1)/float(n_words[artist])))
    sorted_artists = sorted(artists, key=lambda p: -log_probability[p])
    if debug:
        for artist in sorted_artists:
            print("%s: log_probability of %.1f for %s" % (file, log_probability[artist], artist))
    print("%s most resembles the work of %s (log-probability=%.1f)" % (file, sorted_artists[0], log_probability[sorted_artists[0]]))
