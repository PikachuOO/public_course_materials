#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# An input field of type hidden is used to pass an integer
# to successive invocations

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Using A Hidden Variable');
warningsToBrowser(1);

if (defined param('x')) {
    $x = param("x") + 1;
} else {
    $x = 0;
}

printf "2**%d = %d\n", $x, 2 ** $x;

print <<eof;
<form method="post" action="">
<input type=hidden name="x" value="$x">
<input type="submit" value="Next Power of 2">
</form>
</html>
eof
