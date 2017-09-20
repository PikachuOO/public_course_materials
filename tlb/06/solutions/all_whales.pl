#!/usr/bin/perl -w

while ($line = <STDIN>) {
    $line = lc $line;     # convert line to lower case
    $line =~ s/\s+$//;    # remove trailing white space
    $line =~ s/s?$//;     # change to singular
    $line =~ s/\s+/ /g;   # convert sequential white-space charcaters to a single space

    if ($line =~ /(\d+)\s*(.+)\s*$/) {
        $count = $1;
        $species = $2;
        $n_pods{$species}++;
        $n_individuals{$species} += $count;
    } else {
        print "Sorry couldn't parse: $line\n";
    }
}

foreach $species (sort keys %n_pods) {
    print "$species observations: $n_pods{$species} pods, $n_individuals{$species} individuals\n";
}