#!/usr/bin/perl -w

die "Usage $0: <n> <file>\n" if @ARGV != 2;

open F, "<", $ARGV[1] or die "$0: can not open $ARGV[1]: $!\n";
$line_number = 1;
while ($line = <F>) {
	if ($line_number == $ARGV[0]) {
		print $line;
		exit 1;
	}
	$line_number++;
}
exit 0;