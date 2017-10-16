#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# Fetch a web page removing HTML tags and constants
# The contents of script or style tags are removed..
# Non-blank lines are printed
#
# The regex code below doesn't handle a number of cases.  It is often
# better to use a library to properly parse HTML before processing it.
# But beware illegal HTML is common & often causes problems for parsers.
#
# note the use of the s modifier to allow . to match a newline
#


use LWP::Simple;
foreach $url (@ARGV) {
	$html = get $url;
	$html =~ s/<script.*?<\/script>//isg;  # remove script tags including contents
	$html =~ s/<style.*?<\/style>//isg;    # remove style tags including contents
    $html =~ s/<.*?>//isg; # remove tags
    $html =~ s/\n\s*\n/\n/ig;  # blank lines
    print $html;
}
