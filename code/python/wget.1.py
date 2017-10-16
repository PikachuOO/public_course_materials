#!/usr/bin/python
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch a web page remove HTML tags and constants
# and print non-empty lines
#
# The regex code below doesn't handle a number of cases.  It is often
# better to use a library to properly parse HTML before processing it.
# But beware illegal HTML is common & often causes problems for parsers.

import re, sys

# urllib package names changed in Python 3
try:
    from urllib import urlopen # Python 2
except ImportError:
    from urllib.request import urlopen # Python 3

for url in sys.argv[1:]:
    response = urlopen(url)
    webpage = response.read().decode()
    webpage = re.sub(r'(?i)<script>.*?</script>', '', webpage)
    webpage = re.sub(r'(?i)<style>.*?</style>', '', webpage)
    webpage = re.sub(r'&\w+;', ' ', webpage)
    webpage = re.sub(r'<[^>]*>', '', webpage)
    webpage = re.sub(r'\n\s*\n', '\n', webpage)
    sys.stdout.write(webpage)
