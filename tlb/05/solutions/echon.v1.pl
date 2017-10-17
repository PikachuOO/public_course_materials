#!/usr/bin/perl -w
die "Usage: $0 <number of lines> <string>\n" if @ARGV != 2;
die "$0: argument 1 must be a non-negative integer\n" if $ARGV[0] !~ /^\d+$/;
foreach (1..$ARGV[0]) {
    print "$ARGV[1]\n";
}
