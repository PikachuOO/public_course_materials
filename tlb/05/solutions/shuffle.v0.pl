#!/usr/bin/perl -w
# simple implementation of http://en.wikipedia.org/wiki/Fisher-Yates_shuffle
@lines = <>;
print splice(@lines, rand(@lines), 1) while @lines;
