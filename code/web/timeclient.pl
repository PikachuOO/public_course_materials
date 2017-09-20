#!/usr/bin/perl -w
# simple Perl TCP/IP client
# written for COMP2041 by andrewt@cse.unsw.edu.au

use IO::Socket;
$server_host =  $ARGV[0] || 'localhost';
$server_port = 4242;
$c = IO::Socket::INET->new(PeerAddr => $server_host, PeerPort  => $server_port) or die;
$time = <$c>;
close $c;
print "Time is $time\n";
