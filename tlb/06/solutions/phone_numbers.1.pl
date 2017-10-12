#!/usr/bin/perl -w
# there are perl libraries which provide a  better way to fetch web pages
foreach $url (@ARGV) {
    open my $f, '-|', "wget -q -O- $url" or die;
    while ($line = <$f>) {
        @numbers = $line =~ /[\d\- ]+/g;
        foreach $number (@numbers) {
            $number =~ s/\D//g;
            print "$number\n" if length $number >= 8 && length $number <= 15;
        }
    }
    close $f;
}