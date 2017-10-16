#!/usr/bin/perl -w
# delete blank lines from specified files

die "Usage: $0 <files>\n" if !@ARGV;

foreach $file (@ARGV) {
    open my $in, '<', $file or die "Can not open $file: $!";
    @lines = <$in>;  # reads entire file into array
    close $in;
    open my $out, '>', $file or die "Can not open $file: $!";
    foreach $line (@lines) {
        print $out $line if $line !~ /^\s*$/;
    }
    close $out;
}
