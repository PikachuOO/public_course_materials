#!/usr/bin/perl -w

# Simple CGI script written by andrewt@cse.unsw.edu.au
# Demonstrating use of CGI::Carp to redirect errors to browser
# The warning appears as a comment in the HTML source

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Handling warnings in CGI Scripts');
warningsToBrowser(1);
warn "example warning";     # generate a warning
die "example fatal error";  # generate a fatal error
print end_html;
