#!/usr/bin/perl -w

$n_distinct_lines_needed = shift @ARGV or die;

$n_lines = 0;
while ($line = <STDIN>) {
	$n_lines++;
	$line = lc $line;
	$line =~ s/\s//g;
	$lines_seen{$line}++;
	if (keys %lines_seen >= $n_distinct_lines_needed) {
		print "$n_distinct_lines_needed distinct lines seen after $n_lines lines read.\n";
		exit 0;
	}
}
print "End of input reached after $n_lines lines read - $n_distinct_lines_needed different lines not seen.\n";
