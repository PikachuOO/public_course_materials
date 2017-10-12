#!/usr/bin/perl -w
die "Usage: $0 <n>" if @ARGV != 1;
while ($line = <STDIN>) {
	$seen{$line}++;
	if ($seen{$line} >= $ARGV[0]) {
		print "Snap: $line";
		last;
	}
}
