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

param('x', $x);

printf "2**%d = %d\n", $x, 2 ** $x;
print start_form, "\n";
print hidden('x'), "\n";
print submit(value => "Next Power of 2"), "\n";
print end_form, "\n";
print end_html, "\n";
