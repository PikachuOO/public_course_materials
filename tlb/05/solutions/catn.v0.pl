#!/usr/bin/perl -w

if (@ARGV > 0 && $ARGV[0] eq "-n") {
    $doNumbering = 1;
    shift;
}
$nlines = 1;
while (<>) {
    printf "%6d  ",$nlines++ if $doNumbering;
    print;
}
