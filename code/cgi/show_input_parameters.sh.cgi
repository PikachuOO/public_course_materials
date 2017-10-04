#!/bin/sh
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Output some simple HTML and the input parameters
# the web server has passed on to the CGI script.

if test "$REQUEST_METHOD" = POST
then
    parameters="`cat`"
else
    parameters="$QUERY_STRING"
fi

cat <<eof
Content-type: text/html

<!DOCTYPE html>
<html lang="en">
<head></head>
<body>

<h2>$REQUEST_METHOD Request - Input Parameters</h2>
<pre>
$parameters
</pre>
</body>
</html>
eof


