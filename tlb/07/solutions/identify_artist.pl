#!/usr/bin/perl -w
$debug = 0;

foreach $file (glob "lyrics/*") {
    my $artist = $file;
    $artist =~ s/.*\///;
    $artist =~ s/\.txt$//;
    $artist =~ s/_/ /g;
    open my $f, '<', $file or die "can not open $file: $!";;
    while (<$f>) {
        tr/A-Z/a-z/;
        foreach (/[a-z]+/g) {
            $frequency{$artist}{$_}++;
            $n_words{$artist}++;
        }
    }
    close $f;
}

@artists = keys %frequency;
foreach $file (@ARGV) {
    my %log_probability;
    if ($file eq '-d') {
        $debug = 1;
        next;
    }
    open my $f, '<', $file or die "can not open $file: $!";
    while (<$f>) {
        tr/A-Z/a-z/;
        foreach $word (/[a-z]+/g) {
            foreach $artist (@artists) {
                $log_probability{$artist} += log((($frequency{$artist}{$word}||0) + 1)/$n_words{$artist});
            }
        }
    }
    close $f;
    @sorted_artists = sort {$log_probability{$b} <=> $log_probability{$a}} @artists;
    if ($debug) {
        foreach $artist (@sorted_artists) {
            printf "%s: log_probability of %.1f for %s\n", $file, $log_probability{$artist}, $artist;
        }
    }
    printf "%s most resembles the work of %s (log-probability=%.1f)\n", $file, $sorted_artists[0], $log_probability{$sorted_artists[0]};
}
