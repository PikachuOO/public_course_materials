#!/usr/bin/perl -w

$base_url = "http://timetable.unsw.edu.au/current";

foreach $course (@ARGV) {
    my %lectures_seen;
    open my $f, '-|', "wget -q -O- $base_url/$course.html" or die "Can not fetch web page for $course: $!";
    while ($line = <$f>) {
        next if $line !~ /href.*>Lecture</;

        my $session = "";
        $line = <$f>;
        $session = $& if $line =~ /[A-Z][0-9]/;

        <$f> foreach 1..4; # skip 4 lines

        $line = <$f>;
        chomp $line;
        $line =~ s/<.*?>//g;
        $line =~ s/^\s*//g;
        $line =~ s/\s*$//g;

        next if !$line;
        next if $lectures_seen{$line}++;
        print "$course: $session $line\n";
    }
    close $f;
}
