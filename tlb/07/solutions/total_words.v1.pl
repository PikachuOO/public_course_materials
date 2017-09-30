#!/usr/bin/perl -w
$count = 0;
while ($line = <STDIN>) {
    my @words = split /[^a-zA-Z]+/, $line;
    foreach $word (@words) {
        $count++ if $word ne '';
    }
}
print "$count words\n"