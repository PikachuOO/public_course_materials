#!/usr/bin/perl -w

while ($line = <STDIN>) {
	@words = split /\s+/, $line;
	@sorted_words = sort @words;
	print join(" ",@sorted_words), "\n";
}