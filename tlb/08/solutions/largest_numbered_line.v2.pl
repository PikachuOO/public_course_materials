#!/usr/bin/perl -w
push @numbers, /(\-?\d+(?:\.\d+)?)/g foreach @lines = <STDIN>;
exit if !@numbers;
$largest = (sort {$b <=> $a} @numbers)[0];
(sort {$b <=> $a} /(\-?\d+(?:\.\d+)?)/g)[0] == $largest && print foreach @lines;
