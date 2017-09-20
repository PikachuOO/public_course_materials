#!/usr/bin/perl -w
# fetch files via http from the webserver at the specified URL
# see HTTP::Request::Common for a more general solution
# written by andrewt@cse.unsw.edu.au as a COMP2041 lecturer example

use IO::Socket;
foreach $url (@ARGV) {
    $url =~ /http:\/\/([^\/]+)(:(\d+))?(.*)/ or die;
    $c = IO::Socket::INET->new(PeerAddr => $1, PeerPort => $2 || 80) or die;
    # send request for web page to server
    print $c "GET $4 HTTP/1.0\n\n";
    # read what the server returns
    my @webpage = <$c>;
    close $c;
    print "GET $url =>\n", @webpage, "\n";
}
