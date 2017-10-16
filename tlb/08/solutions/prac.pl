#!/usr/local/bin/perl
#
# Prac Exam Exercise
# Author: John Shepherd (sample solution)
#

while (<>) {
    chomp;
    my ($sid,$ex,$tests,$warns) = split;
    if ($tests == 5) {
        $mark = 10;
        $ncorrect{"$sid"}++;
    }
    else {
        $mark = $tests/2.0;
    }
    $mark -= 2 if ($warns > 0);
    $mark = 0 if ($mark < 0);
    $total{$sid} += $mark;
}

foreach $sid (sort keys %total) {
    if ($ncorrect{$sid} >= 2) {
        $passfail = "PASS";
    } else {
        $passfail = "FAIL";
    }
    printf "%s %4.1f %s\n", $sid, $total{$sid}, $passfail;
}
