#!/usr/bin/perl -w
foreach $arg (@ARGV) {
    if ($arg eq "--version") {
        print "$0: version 0.1\n";
        exit 0;
    }
    # handle other options
    # ...
    else {
        push @files, $arg;
    }
}
foreach $f (@files) {
    open F, '<', $f or die "$0: Can't open $f: $!\n";
    # process F
    #...
    close F;
}
