#!/usr/bin/perl -w

foreach $prefix (@ARGV) {
    open my $f, '-|', "wget -q -O- http://www.timetable.unsw.edu.au/current/${prefix}KENS.html" or die;
    while (<$f>) {
        print "$1\n" if />($prefix\d\d\d\d)</;
    }
    close $f;
}
