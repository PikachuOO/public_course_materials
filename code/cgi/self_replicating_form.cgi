#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script

print <<eof
Content-type: text/html

<html><head><title>Self replicating Form</title></head><body>
<form method="post" action="">
<input type="submit">
</form>
</body>
</html>
eof

