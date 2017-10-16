#!/usr/bin/perl -w

# print an extra trailing space

foreach $argument (@ARGV) {
	if (!$seen{$argument}) {
		print "$argument ";
		$seen{$argument} = 1;
	}
}

print "\n";
