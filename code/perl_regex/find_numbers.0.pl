#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP[29]041 lecture example

# Find the positive integers among input text
# print their sum and mean

# Note regexp to split on non-digits
# Note check to handle empty string from split

@input_text_array = <>;
$input_text_array = join "", @input_text_array;

@numbers = split(/\D+/, $input_text_array);
print join(",", @numbers), "\n";

foreach $number (@numbers) {
	if ($number ne '') {
		$total += $number;
		$n++;
	}
}

if (@numbers) {
	printf "$n numbers: total $total mean %s\n", $total/$n;
}
