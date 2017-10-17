#!/usr/bin/perl -w
die "Usage: $0 <number of lines> <string>\n" if @ARGV != 2;
die "$0: argument 1 must be a non-negative integer\n" if $ARGV[0] !~ /^\d+$/;
print "$ARGV[1]\n" foreach 1..$ARGV[0];
