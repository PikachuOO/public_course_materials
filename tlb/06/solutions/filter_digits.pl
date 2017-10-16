#!/usr/bin/perl -w

while ($line = <STDIN>) {
    $line =~ s/\d//g;
    print $line;
}
