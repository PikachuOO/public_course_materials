#!/usr/bin/perl -w
die "Usage $0 <n> <m> <column-width>" if @ARGV != 3;
$n = $ARGV[0];
$m = $ARGV[1];
$width = $ARGV[2];
$format = "%${width}d";
foreach $x (1..$n) {
    printf $format, $x;
    foreach $y (1..$m) {
        printf "%${width}d", $x*$y;
    }
    print "\n";
}
