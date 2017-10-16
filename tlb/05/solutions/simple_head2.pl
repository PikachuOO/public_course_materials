#!/usr/bin/perl -w
print ((<STDIN>)[0..(@ARGV&&-$ARGV[0]||10)-1]);
