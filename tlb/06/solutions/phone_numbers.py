#!/usr/bin/python
import sys, re, subprocess
# there are python libraries which provide a  better way to fetch web pages
for url in sys.argv[1:]:
    webpage = subprocess.Popen(["wget","-q","-O-",url], stdout=subprocess.PIPE).communicate()[0]
    for number in re.findall(r'[\d \-]+', webpage):
        number = re.sub(r'\D', '', number)
        if len(number) >= 8 and len(number) <= 15:
            print(number)
