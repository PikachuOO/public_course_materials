#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# The value entered last time is made the initial value
# of the text field

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Initializing A Form');
warningsToBrowser(1);

$last_value = param("string");
if (defined $last_value) {
    print "Last time you entered: $last_value\n";
    $value = "";
} else {
    $value = "initial value";
}

print <<eof;
<form method="post" action="">
Enter a string: <input type="text" name="string" value="$value">
</form>
</html>
eof
