#!/usr/bin/perl -w
if (@ARGV && $ARGV[0] eq "-v") {
    $doOpposite = 1;
    shift @ARGV;
}
$pattern = shift @ARGV;
print grep {$doOpposite^/$pattern/} <>;
