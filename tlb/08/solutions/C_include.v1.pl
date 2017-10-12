#!/usr/bin/perl -w
# Given C source files interpolate #include "FILE" directives recursively.
sub include_file($);

sub include_file($) {
    my ($file) = @_;
    # this function is recursive so a local filehandle is essential
    open my $f, '<', $file or die "$0: can not open $file: $!";
    while ($line = <$f>) {
        if ($line =~ /^#\s*include\s*"([^"]*)"/) {
            include_file($1);
        } else {
            print $line;
        }
    }
    close $f;
}

foreach $file (@ARGV) {
    include_file($file);
}