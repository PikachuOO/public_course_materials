#!/usr/bin/perl -w
# Written by andrewt@cse.unsw.edu.au as a COMP2041 lecture example
# list to port 2041 for incoming connections
# print then details to stdout
# then send back a 404 status code 

use IO::Socket;
$server = IO::Socket::INET->new(LocalPort => 2041, ReuseAddr => 1, Listen => SOMAXCONN) or die;

print "Access this server at http://localhost:2041/\n\n";

while ($c = $server->accept()) {
    printf "HTTP request from %s =>\n\n", $c->peerhost;
    while ($request_line = <$c>) {
        print "$request_line";
        last if $request_line !~ /\S/;
    }
    print $c "HTTP/1.0 404 This webserver always returns a 404 status code\n";
    close $c;
}
