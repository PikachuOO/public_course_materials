#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Count words in text area, file or URL.

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header;
print start_html('Word Count');

my $uploaded_file = param('filename');
if (defined $uploaded_file) {
    my ($lines, $words, $bytes);
    while ($line = <$uploaded_file>) {
        my @words = split /\s+/, $line;
        $words += @words;
        $bytes += length $line;
        $lines++;
    }
    printf "$uploaded_file: %d lines %d words %d bytes\n", $lines, $words, $bytes;
} 

print start_form, "\n",
      filefield('filename'),  "\n",
      submit('Word Count File'), "\n",
      end_form, "\n",
      end_html;
