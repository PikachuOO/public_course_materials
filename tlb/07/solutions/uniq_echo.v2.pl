#!/usr/bin/perl
print join(" ", grep(!$seen{$_}++, @ARGV)), "\n"
