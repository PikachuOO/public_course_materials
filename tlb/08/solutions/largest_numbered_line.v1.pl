#!/usr/bin/perl -w

while ($line = <STDIN>) {
	my @line_numbers = $line =~ /(\-?\d+(?:\.\d+)?)/g;
	if (@line_numbers) {
		my $largest_line_number = (sort {$b <=> $a} @line_numbers)[0];
		push @numbers, $largest_line_number;
		push @lines, $line;
	}
}

if (@numbers) {
	my $largest_number = (sort {$b <=> $a} @numbers)[0];
	foreach $i (0..$#numbers) {
		if ($numbers[$i] == $largest_number) {
			print $lines[$i];
		}
	}
}
