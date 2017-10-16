#!/usr/bin/python

import sys, time, subprocess, re

year = time.localtime().tm_year
url_base = "http://www.handbook.unsw.edu.au"
debug = 0

def prereq(course):
    if debug: print("prereq(%s)" % course)
    ugrad_url = "%s/undergraduate/courses/%d/%s.html" % (url_base, year, course)
    pgrad_url = "%s/postgraduate/courses/%d/%s.html" % (url_base, year, course)

    # there are python libraries which provide a  better way to fetch web pages
    # subprocess.check_output is also usually better, but here we may get a non-zero exit
    # if either pgrad or ugrad page doesn't exist
    webpage = subprocess.Popen(["wget","-q","-O-", ugrad_url, pgrad_url], stdout=subprocess.PIPE).communicate()[0]
    webpage = webpage.decode("utf-8") # assume hansdbook uses 'utf-8'
    listed_prereqs = []
    for line in webpage.split('\n'):
        # look for pre-requisite line handling varying format used  in handbook pages
        if re.search(r'pre.?(requisite)?(.?:|\s+[A-Z]{4}\d{4})', line, re.I):
            line = line.upper()
            line = re.sub(r'<[^>]*>', '', line)
            line = re.sub(r'EXCLU.*', '', line)
            for word in re.findall(r'[A-Z]{4}\d{4}', line):
                listed_prereqs.append(word)
    for course in listed_prereqs:
        if course not in prereqs:
            prereqs[course] = 1
            if recursive:
                prereq(course)

if __name__== "__main__":
    recursive = 0
    prereqs = {}
    for arg in sys.argv[1:]:
        if arg == "-r":
            recursive = 1
        else:
            prereq(arg)
    for course in sorted(prereqs.keys()):
        print(course)
