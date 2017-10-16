#!/usr/bin/perl -w
die "Usage: $0 <n> <m> <file" if @ARGV != 3;
open my $f, '<', $ARGV[2] or die "$0: can not open $ARGV[2]: $!";
while ($line = <$f>) {
    chomp $line;
    @chars = split //, $line;
    print @chars[$ARGV[0]-1..$ARGV[1]-1], "\n";
}
