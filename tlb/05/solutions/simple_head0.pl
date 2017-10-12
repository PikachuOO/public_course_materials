#!/usr/bin/perl -w
$n_lines = 10;
if (@ARGV && $ARGV[0] =~ /-[0-9]+/) {
    $n_lines = $ARGV[0];
    $n_lines =~ s/-//;
    shift @ARGV;
}
$n = 1;
while (<STDIN>) {
    if ($n++ > $n_lines) {
        last;
    }
    print;
}
