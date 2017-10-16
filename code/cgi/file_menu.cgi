#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Create a pop menu with one entry for every file with
# the suffix .cgi in the current directory

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Choosing A File');
warningsToBrowser(1);

@cgi_files = glob("*.cgi");
$default = $cgi_files[rand @cgi_files]; # pick an element at random

print start_form, "\n",
    popup_menu('CGI files', \@cgi_files,  $default), "\n",
    end_form, "\n",
    end_html;
