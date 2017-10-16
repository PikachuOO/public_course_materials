#!/usr/bin/perl -w

while (<STDIN>) {
	s/\s//g;
	$lines_seen{lc $_}++;
	if (keys %lines_seen >= $ARGV[0]) {
		print "$n_distinct_lines_needed distinct lines seen after $. lines read.\n";
		exit 0;
	}
}

print "End of input reached after $. lines read - $ARGV[0] different lines not seen.\n";
