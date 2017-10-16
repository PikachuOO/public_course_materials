#!/usr/bin/python
import sys, subprocess, re

year = 2016
url_base = "http://www.handbook.unsw.edu.au"

prereqs = []
for course in sys.argv:
    ugrad_url = "%s/undergraduate/courses/%d/%s.html" % (url_base, year, course)
    pgrad_url = "%s/postgraduate/courses/%d/%s.html" % (url_base, year, course)

    # there are python libraries which provide a  better way to fetch web pages
    # subprocess.check_output is also usually better, but here we may get a non-zero exit
    # if either pgrad or ugrad page doesn't exist
    webpage = subprocess.Popen(["wget","-q","-O-", ugrad_url, pgrad_url], stdout=subprocess.PIPE).communicate()[0]
    webpage = webpage.decode("utf-8") # guess the encoding
    for line in webpage.split('\n'):
        # look for pre-requisite line handling varying format used  in handbook pages
        if re.search(r'pre.?(requisite)?(.?:|\s+[A-Z]{4}\d{4})', line, re.I):
            line = line.upper()
            line = re.sub(r'<[^>]*>', '', line)
            line = re.sub(r'EXCLU.*', '', line)
            for word in re.findall(r'[A-Z]{4}\d{4}', line):
                prereqs.append(word)

for course in sorted(prereqs):
    print(course)
