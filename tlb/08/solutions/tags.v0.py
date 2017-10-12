#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch specified web pages and count the HTML tags in them
#
# There are python libraries which provide a  better way to fetch web pages
#
# subprocess.check_output was introduced in Python 2.7.
# In previous version you might use:
# webpage = subprocess.Popen(["wget","-q","-O-",url], stdout=subprocess.PIPE).communicate()[0]
#
#
# The regex code below doesn't handle a number of cases.  It is often
# better to use a library to properly parse HTML before processing it.
# But beware illegal HTML is common & often causes problems for parsers.

import sys, re, subprocess, collections
tag_count = collections.defaultdict(lambda:0)

for url in sys.argv[1:]:
    webpage = subprocess.check_output(["wget","-q","-O-",url], universal_newlines=True)
    webpage = re.sub(r'<!--.*?-->','', webpage) # remove comments
    webpage = webpage.lower()
    for tag in re.findall(r'<\s*(\w+)', webpage):
        if tag:
            tag_count[tag] += 1
for tag in sorted(tag_count.keys()):
    print("%s %d"%(tag, tag_count[tag]))
