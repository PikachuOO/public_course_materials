#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# An input field of type hidden is used to pass an integer
# to successive invocations
# Two submit buttons are used to produce different actions

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print <<eof;
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Handling Multiple Submit Buttons</title>
</head>
<body>
eof
warningsToBrowser(1);

$hidden_variable = param("x") || 0;

if (defined param("increment")) {
	$hidden_variable++;
} elsif (defined param("decrement")) {
	$hidden_variable--;
}

print <<eof;
<h2>$hidden_variable</h2>
<form method="post" action="">
<input type=hidden name="x" value="$hidden_variable">
<input type="submit" name="increment" value="Increment">
<input type="submit" name="decrement" value="Decrement">
</form>
</body>
</html>
eof
