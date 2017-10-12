#!/usr/bin/perl -w

open F, '<', $ARGV[0] or die;
@lines = <F>;
close F;

if (!@lines) {
	# no lines
} elsif (@lines % 2 == 1) {
	# odd number of lines
	print $lines[$#lines/2];
} else {
	# even number of lines
	print $lines[$#lines/2];
	print $lines[$#lines/2 + 1];
}
