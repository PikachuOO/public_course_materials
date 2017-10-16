#!/usr/bin/perl -w

$dataset = "dataset-medium";

sub student_post_filenames {
	my ($student) = @_;
	
	my @post_filenames = glob "$dataset/$student/*.txt";
	return reverse sort @post_filenames;
}

foreach $student (@ARGV) {
	print join(" ", student_post_filenames($student)), "\n";
}
