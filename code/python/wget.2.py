#!/usr/bin/python2
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch a web page remove HTML tags and constants
# using HTML parser BeautifulSoup
# and print non-empty lines

import re, sys
from urllib import urlopen
import BeautifulSoup

# on Python 3 instead do
# from urllib.request import urlopen # Python 3
# import bs4 as BeautifulSoup
# and change BeautifulSoup(webpage) to BeautifulSoup(webpage, "lxml")

def traverse(html):
    if isinstance(html, BeautifulSoup.Tag):
        if html.name in ['style', 'script']:
            return ""
        else:
            return traverse(html.contents)
    elif isinstance(html, list):
        return "".join([traverse(h) for h in html])
    else:
        return html

for url in sys.argv[1:]:
    webpage = urlopen(url).read().decode()
    soup = BeautifulSoup.BeautifulSoup(webpage)
    text = traverse(soup)
    text = re.sub(r'\n\s*\n', '\n', text)
    sys.stdout.write(text)
