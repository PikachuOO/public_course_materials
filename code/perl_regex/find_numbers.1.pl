#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP[29]041 lecture example

# Find integers (positive and negative) among input text
# print their sum and mean

# Note regexp to match number:  -?\d+
# Harder to use split here (unlike just positive integers)

@input_text_array = <>;
$input_text_array = join "", @input_text_array;

@numbers = $input_text_array =~ /-?\d+/g;

foreach $number (@numbers) {
	$total += $number;
}

if (@numbers) {
	$n = @numbers;
	printf "$n numbers: total $total mean %s\n", $total/$n;
}
