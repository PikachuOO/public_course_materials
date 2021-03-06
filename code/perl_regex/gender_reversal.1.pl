#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# For each file given as argument replace occurrences of Hermione
# allowing for some misspellings with Harry and vice-versa.
# Relies on Zaphod not occurring in the text.
# Modified text is stored in an array then
# the file is over-written

foreach $filename (@ARGV) {
    open my $f, '<', $filename or die "$0: Can not open $filename: $!";
    $line_count = 0;
    while ($line = <$f>) {
        $line =~ s/Herm[io]+ne/Zaphod/g;
        $line =~ s/Harry/Hermione/g;
        $line =~ s/Zaphod/Harry/g;
        $new_lines[$line_count++] = $line;
    }
    close $f;
    open my $g, '>', ">$filename" or die "$0: Can not open $filename : $!";
    print $g @new_lines;
    close $g;
}
