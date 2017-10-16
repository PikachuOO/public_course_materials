#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au for COMP2041
# count lines of C source code
$total = 0;
foreach $file (glob("*.[ch]")) {
    open my $f, '<', $file or die "Can not open $file: $!";
    @lines = <$f>;
    $n_lines = @lines;
    # Why wouldn't   $n_lines = <FILE>;   work?

    printf "%7d %s\n", $n_lines, $file;
    $total += $n_lines;
    close $f;
}
printf "%7d total\n", $total;
