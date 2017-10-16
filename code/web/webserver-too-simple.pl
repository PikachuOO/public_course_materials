#!/usr/bin/perl -w

# return files in response to incoming http requests to port 2041
# note does not check the request is well-formed or that the file exists
# also very insecure as pathname may contain ..
# written by andrewt@cse.unsw.edu.au as COMP2041 lecture example

use IO::Socket;

print "Access this server at http://localhost:2041/\n\n";

while (1) {
    $server = IO::Socket::INET->new(LocalPort => 2041, ReuseAddr => 1, Listen => SOMAXCONN) or die;
    while ($c = $server->accept()) {
        my $request = <$c>;
        print "Connection from ", $c->peerhost, ": $request";
        $request =~ /^GET (.+) HTTP\/1.[01]\s*$/;
        print "Sending back /home/cs2041/public_html/$1\n";
        open my $f, '<',"/home/cs2041/public_html/$1";
        $content = join "", <$f>;
        close $f;
        print $c "HTTP/1.0 200 OK\n";
        print $c "Content-Type: text/html\n";
        printf $c "Content-Length: %d\n\n", length($content);
        print $c $content;
        close $c;
    }
}
