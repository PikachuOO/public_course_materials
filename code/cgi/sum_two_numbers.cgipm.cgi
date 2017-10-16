#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Sum two numbers and outputs a form which will rerun the script

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Sum Two Numbers');
warningsToBrowser(1);

$x = param("x");
$y = param("y");
if (defined $x && defined $y) {
    printf "%s + %s = %s\n", $x, $y, $x + $y;
}

print start_form, "\n";
print 'Enter x: ', textfield('x'), "\n";
print p;
print 'Enter y: ', textfield('y'), "\n";
print p, "\n";
print submit, "\n";
print end_form,"\n";
print end_html;
