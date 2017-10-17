#!/usr/bin/perl -w
if (@ARGV != 2) {
    die "Usage: $0 <number of lines> <string>\n";
}
if ($ARGV[0] !~ /^\d+$/) {
    die "$0: argument 1 must be a non-negative integer\n";
}
foreach ($i=0; $i < $ARGV[0]; $i++) {
    print "$ARGV[1]\n";
}
