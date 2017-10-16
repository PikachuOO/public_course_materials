#!/usr/bin/perl -w
# print words in file 1 but not file 2

die "Usage: $0 <file1> <file2>\n" if @ARGV != 2;

open my $f, '<', $ARGV[0] or die "Can't open $ARGV[0]: $!";
while ($word = <$f>) {
    chomp $word;
    $w{$word} = "added";
}
close $f;

open my $g, '<', $ARGV[1] or die "Can't open $ARGV[1]: $!";
while ($word = <$g>) {
    chomp $word;
    $w{$word} = "deleted";
}
close $g;

foreach $word (sort keys %w) {
    print "$word\n" if $w{$word} ne "deleted";
}
