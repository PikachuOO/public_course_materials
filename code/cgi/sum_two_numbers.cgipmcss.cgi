#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Sum two numbers and outputs a form which will rerun the script

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header;
print start_html(-title=>'Sum Two Numbers',-style=>{-src=>['sum_two_numbers.css']});
warningsToBrowser(1);

if (defined param("x") && defined param("y")) {
    printf "%s + %s = %s\n", param('x'), param('y'), param('x') + param('y');
}

print h1('Sum Two Numbers');

print start_form;
print span(
    {-class=>'class1'},
    'Enter x: ',
    textfield('x')
    );
print p;
print span(
    {-id=>'id1'},
    'Enter y: ',
    textfield('y')
    );
print p;
print submit;
print end_form;
print end_html;
