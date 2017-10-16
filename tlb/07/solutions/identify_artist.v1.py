#!/usr/bin/python

import sys, glob, re, collections, os, math

frequency = {}
for f in glob.glob("lyrics/*.txt"):
    lines = open(f).read().lower()
    author = os.path.splitext(os.path.basename(f))[0].replace('_', ' ')
    words = re.findall(r'[a-z]+', lines, flags=re.S | re.M | re.I)
    count = collections.Counter(words)
    # we need to use a default value to capture at creation time, not runtime
    # the following line just says the dictionary defaults to log(1/|words|)
    frequency[author] = collections.defaultdict(lambda x=math.log(float(1) / len(words)): x)
    for word, occurances in count.items():
        frequency[author][word] = math.log(float((occurances + 1)) / len(words))

for f in sys.argv[1:]:
    lines = open(f).read().lower()
    words = re.findall(r'[a-z]+', lines, flags=re.I)
    prob = {}
    for author, freq in frequency.items():
        prob[author] = sum(freq[word] for word in words)
    likely = max(prob, key=prob.get) # this is how you sort hashes by value in python
    print("%s most resembles the work of %s (log-probability=%.1f)" % (f, likely, prob[likely]))
