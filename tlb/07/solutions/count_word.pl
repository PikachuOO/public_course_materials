#!/usr/bin/perl -w
die "Usage: $0 <word>\n" if @ARGV != 1;
$specified_word = lc $ARGV[0];
$count = 0;
while ($line = <STDIN>) {
    $line = lc $line;
    my @words = split /[^a-z]+/i, $line;
    foreach $word (@words) {
        $count++ if $word eq $specified_word;
    }
}
print "$specified_word occurred $count times\n"