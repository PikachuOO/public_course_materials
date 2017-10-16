#!/usr/bin/perl -w
# writen by andrewt@cse.unsw.edu.au as a COMP2041 example
# sum integers supplied as command line arguments
# no check that aguments are numeric

$sum = 0;
foreach $arg (@ARGV) {
	$sum += $arg;
}
print "Sum of the numbers is $sum\n";
