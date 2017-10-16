#!/bin/sh
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Sum two numbers and outputs a form which will rerun the script


# Note removal of characters other than 0-9 . - + to avoid potential security problems

if test $REQUEST_METHOD = "GET"
then
    parameters="$QUERY_STRING"
else
    read parameters
fi

x=`echo $parameters|sed '
    s/.*x=//
    s/&.*//
    s/[^0-9\-\.\+]//g
    '`
y=`echo $parameters|sed '
    s/.*y=//
    s/&.*//
    s/[^0-9\-\.\+]//g
    '`

cat <<eof
Content-type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<title>Sum Two Numbers</title>
</head>
<body>
eof

sum="?"
test "$x" -a "$y" && sum=`expr "$x" '+' "$y"`

cat <<eof

<form method="GET" action="">
<input type=textfield name=x value=$x>
+
<input type=textfield name=y value=$y>
=
$sum
<input type="submit" value="calculate">
</form>
</body>
</html>
eof

