#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# Print the last number (real or integer) on every line if there is one.
# Note regexp to match number:  -?\d+(\.\d+)?

while ($line = <>) {
	if ($line =~ /(-?\d+(\.\d+)?)\D*$/) {
		print "$1\n";
	}
}
