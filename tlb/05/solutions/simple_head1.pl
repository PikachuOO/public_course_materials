#!/usr/bin/perl -w
$n_lines = 10;
if (@ARGV && $ARGV[0] =~ /-[0-9]+/) {
    $n_lines = shift @ARGV;
    $n_lines =~ s/-//;
}
@lines = <STDIN>;
print @lines[0..$n_lines-1];
