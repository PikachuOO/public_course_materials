#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 example
# fetch specified web page and count the HTML tags in them

# The regex code below doesn't handle a number of cases.  It is often
# better to use a library to properly parse HTML before processing it.
# But beware illegal HTML is common & often causes problems for parsers.

use LWP::Simple;

$sort_by_frequency = 0;
foreach $arg (@ARGV) {
    if ($arg eq "-f") {
        $sort_by_frequency = 1;
    } else {
        push @urls, $arg;
    }
}
foreach $url (@urls) {
    $webpage = get $url;
    $webpage =~ tr/A-Z/a-z/;
    $webpage =~ s/<!--.*?-->//g; # remove comments
    @tags = $webpage =~ /<\s*(\w+)/g;
    foreach $tag (@tags) {
        $tag_count{$tag}++;
    }
}
if ($sort_by_frequency) {
    @sorted_tags = sort {$tag_count{$a} <=> $tag_count{$b} || $a cmp $b} keys %tag_count;
} else {
    @sorted_tags = sort keys %tag_count;
}
print "$_ $tag_count{$_}\n" foreach @sorted_tags;
