#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# count how many people enrolled in each course

open my $f, '<', "course_codes" or die "$0: can not open course_codes: $!";
while ($line = <$f>) {
    chomp $line;
    $line =~ /([^ ]+) (.+)/ or die "$0: bad line format '$line'";
    $course_names{$1} = $2;
}
close $f;

while ($course = <>) {
    chomp $course;
    $course =~ s/\|.*//;
    $count{$course}++;
}

foreach $course (sort keys %count) {
    print "$course_names{$course} has $count{$course} students enrolled\n";
}
