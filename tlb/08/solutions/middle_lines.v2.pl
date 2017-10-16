#!/usr/bin/perl -w
@lines = <STDIN>;
print @lines[(@lines-1)/2..((@lines-1)/2 + 1 - (@lines%2))] if @lines;
