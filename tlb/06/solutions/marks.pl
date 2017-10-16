#!/usr/bin/perl -w
while (<>) {
    chomp;
    ($sid,$mark) = split;
    if ($mark !~ /^\d+$/) {
        $grade = "??";
    }
    else {
        $grade = "FL" if $mark >= 0 && $mark < 50;
        $grade = "PS" if $mark >= 50 && $mark < 65;
        $grade = "CR" if $mark >= 65 && $mark < 75;
        $grade = "DN" if $mark >= 75 && $mark < 85;
        $grade = "HD" if $mark >= 85 && $mark <= 100;
        $grade = "??" if $mark < 0 || $mark > 100;
    }
    $err = ($grade ne "??") ? "" : " ($mark)";
    print "$sid $grade$err\n";
}