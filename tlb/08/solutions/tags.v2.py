#!/usr/bin/python2
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch a web page remove HTML tags, constants,
# text between script blank lines
# and print non-empty lines

import sys, re, collections

from urllib import urlopen
import BeautifulSoup

# on Python 3 instead do
# from urllib.request import urlopen # Python 3
# import bs4 as BeautifulSoup
# and change BeautifulSoup(webpage) to BeautifulSoup(webpage, "lxml")

if len(sys.argv) > 1 and sys.argv[1] == "-f":
    sort_by_frequency = 1
    urls = sys.argv[2:]
else:
    sort_by_frequency = 0
    urls = sys.argv[1:]

tag_count = collections.defaultdict(lambda:0)
for url in urls:
    webpage = urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(webpage)
    for tag in soup.findAll():
        tag_count[tag.name] += 1

if sort_by_frequency:
    # sort on a tuple of (tag frequency, tag name)
    # so tags are order first by frequency then by name
    ordered_tags = sorted(tag_count.keys(), key=lambda t: (tag_count[t],t))
else:
    ordered_tags = sorted(tag_count.keys())
for tag in ordered_tags:
    print("%s %d"%(tag, tag_count[tag]))
