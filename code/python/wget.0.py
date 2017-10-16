#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch a web page remove HTML tags, constants,
# text between script blank lines
# and print non-empty lines.
#
# There are python libraries which provide a  better way to fetch web pages
#
# subprocess.check_output was introduced in Python 2.7.
# In older Pythons version you might use:
# webpage = subprocess.Popen(["wget","-q","-O-",url], stdout=subprocess.PIPE).communicate()[0]
#
# The regex code below doesn't handle a number of cases.  It is often
# better to use a library to properly parse HTML before processing it.
# But beware illegal HTML is common & often causes problems for parsers.

import sys, re, subprocess
for url in sys.argv[1:]:
    webpage = subprocess.check_output(["wget", "-q", "-O-", url], universal_newlines=True)
    webpage = re.sub(r'(?i)<script>.*?</script>', '', webpage)
    webpage = re.sub(r'(?i)<style>.*?</style>', '', webpage)
    webpage = re.sub(r'&\w+;', ' ', webpage)
    webpage = re.sub(r'<[^>]*>', '', webpage)
    webpage = re.sub(r'\n\s*\n', '\n', webpage)
    sys.stdout.write(webpage)
