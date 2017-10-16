#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# Read numbers until end of input (or a non-number)  is reached
# then print the sum of the numbers

$sum = 0;
while ($line = <STDIN>) {
    $line =~ s/^\s*//; # remove leading white space
    $line =~ s/\s*$//; # remove leading trailing white space
    # Test if string looks like an integer or real (scientific notation not handled!)
    if ($line !~ /^\d[.\d]*$/) {
        last;
    }
    $sum += $line;
}
print "Sum of the numbers is $sum\n";
