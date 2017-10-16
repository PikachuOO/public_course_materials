#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# Fetch a web page removing HTML tags and constants (e.g &amp;)
# Lines between script or style tags are skipped.
# Non-blank lines are printed

# There are better ways to fetch web pages (e.g. HTTP::Request::Common)
# The regex code below doesn't handle a number of cases.  It is often
# better to use a library to properly parse HTML before processing it.
# But beware illegal HTML is common & often causes problems for parsers.

foreach $url (@ARGV) {
    open my $f, '-|', "wget -q -O- '$url'" or die;
    while ($line = <$f>) {
        if ($line =~ /^\s*<(script|style)/i) {
            while ($line = <$f>) {
                last if $line =~ /^\s*<\/(script|style)/i;
            }
        } else {
            $line =~ s/&\w+;/ /g;
            $line =~ s/<[^>]*>//g;
            print $line if $line =~ /\S/;
        }
    }
    close $f;
}
