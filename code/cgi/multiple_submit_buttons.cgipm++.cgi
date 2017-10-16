#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Outputs a form which will rerun the script
# An input field of type hidden is used to pass an integer
# to successive invocations
# Two submit buttons are used to produce different actions

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Handling Multiple Submit Buttons');
warningsToBrowser(1);

$hidden_variable = param("x") || 0;

if (defined param("increment")) {
	$hidden_variable++;
} elsif (defined param("decrement")) {
	$hidden_variable--;
}

param('x', $hidden_variable);
print h2($hidden_variable), "\n",
      start_form, "\n",
      hidden('x'), "\n",
      submit('increment'), "\n",
      submit('decrement'), "\n",
      end_form, "\n",
      end_html;
