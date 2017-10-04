#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# An input field of type hidden is used to pass an integer
# to successive invocations

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Alternating State');
warningsToBrowser(1);

$x = param('state') || 0;
$x++;
param("state", $x);

print start_form, "\n";

if ($x % 2 == 0) {
    print "What's your name?\n", textfield('name');
} else {
    print "What's your height?\n", textfield('height');
}

print hidden('state'), "\n";
print end_form, "\n";
print end_html, "\n";
