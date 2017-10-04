#!/usr/bin/python
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Count words in a file.

import cgi, cgitb, re

print """Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<title>Word Count</title>
</head>
<body>
"""

cgitb.enable()
parameters = cgi.FieldStorage()

if 'filename' in parameters:
    uploaded_file =parameters['filename'].file
    (lines, words, bytes) = (0, 0, 0)
    for line in uploaded_file:
        words += len(re.split(r'/\s+/', line))
        bytes += len(line)
        lines += 1
    print "%s: %d lines %d words %d bytes\n" % (parameters['filename'].filename, lines, words, bytes)

print """
<form method="post" action="" enctype="multipart/form-data">
<input type="file" name="filename" value="Bitter.html">
<input type="submit" name="action" value="Word Count File">
</form>
</body>
</html>
"""
