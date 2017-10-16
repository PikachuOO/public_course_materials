#!/usr/bin/perl -w

# Simple CGI script written by andrewt@cse.unsw.edu.au
# Print some HTML plus the environment
# passed to CGI script by the web server
# Note a < character in environment variable values will be interpreted as a HTML tag

print "Content-type: text/html

<html>
<head></head>
<body>
<h2>Environment Variables</h2>
<pre>
";

system "env";

print "
</pre>
</body>
</html>
";

