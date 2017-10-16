#!/usr/bin/python

# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch a web page remove HTML tags, constants,
# text between script blank lines
# and print non-empty lines

# The regex code below doesn't handle a number of cases.  It is often
# better to use a library to properly parse HTML before processing it.
# But beware illegal HTML is common & often causes problems for parsers.

import sys, re, collections

# urllib package names changed in Python 3
try:
    from urllib import urlopen # Python 2
except ImportError:
    from urllib.request import urlopen # Python 3

if len(sys.argv) > 1 and sys.argv[1] == "-f":
    sort_by_frequency = 1
    urls = sys.argv[2:]
else:
    sort_by_frequency = 0
    urls = sys.argv[1:]

tag_count = collections.defaultdict(lambda:0)
for url in urls:
    webpage = urlopen(url).read().decode('utf-8')  # would be better to check encoding rather than assume utf-8
    webpage = re.sub(r'<!--.*?-->','', webpage)    # remove comments
    webpage = webpage.lower()
    for tag in re.findall(r'<\s*(\w+)', webpage):
        if tag:
            tag_count[tag] += 1

if sort_by_frequency:
    # sort on a tuple of (tag frequency, tag name)
    ordered_tags = sorted(list(tag_count.keys()), key=lambda t: (tag_count[t],t))
else:
    ordered_tags = sorted(tag_count.keys())
for tag in ordered_tags:
    print("%s %d"%(tag, tag_count[tag]))
