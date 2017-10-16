#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# Count the number of lines on standard input - using backwards while to be really concise

$line_count = 0;
$line_count++ while <STDIN>;
print "$line_count lines\n";
