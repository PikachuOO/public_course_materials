#!/usr/bin/perl -w

# return files in response to incoming http requests
# files with suffix .cgi executed and output returned
# GET & POST requests handled
# assumes application/x-www-form-urlencoded data so CGI.pm won't work
# andrewt@cse.unsw.edu.au

# See http://search.cpan.org/dist/HTTP-Server-Simple/
# for a much  more general solution

use IO::Socket;
$server = IO::Socket::INET->new(LocalPort => 2041, ReuseAddr => 1, Listen => SOMAXCONN) or die;

print "Access this server at http://localhost:2041/\n\n";

while ($c = $server->accept()) {
    my $request = <$c>;
    printf "Connection from %s, request: $request", $c->peerhost;
    my $content_length = 0;
    while (<$c>) {
        print;
        $header_field{$1} = $2 if /(\S+):\s*(.*)/;
        last if /^\s*$/;
    }
    if ($request =~ /^(GET|POST) (.+) HTTP\/1.[01]\s*$/) {
        my $method = $1;
        my $url = $2;
        $url =~ s/(^|\/)\.\.(\/|$)//g;
        if ($url =~ /^(.*\.cgi)(\?(.*))?$/) {
            my $cgi_script = "/home/cs2041/public_html/$1";
            my $parameters = '';
            if ($method eq 'GET') {
                $parameters = $3 if $3;
            } else {
                read($c, $parameters, $header_field{'Content-Length'});
            }
            print $c "HTTP/1.0 200 OK\n";
            print "Running: echo '$parameters'|$cgi_script\n";
            # provide a minimal set of environment variables
            %ENV = (CONTENT_LENGTH => length $parameters,
                    CONTENT_TYPE => 'application/x-www-form-urlencoded',
                    REQUEST_METHOD => $method,
                    REQUEST_URI => $url,
                    SCRIPT_NAME => $cgi_script);
            # obvious security hole here from shell meta-characters in parameters
            print $c `echo '$parameters'|$cgi_script`;
        } else {
            my $file = "/home/cs2041/public_html/$url";
            $file .= "/index.html" if -d $file;
            if (!-e $file) {
                print $c "HTTP/1.0 404 FILE NOT FOUND\nContent-Type: text/plain\n\nFile $file not found\n";
            } else {
                print $c "HTTP/1.0 200 OK\nContent-Type: text/html\n\n";
                open my $f, '<', $file or die;
                print $c (<$f>);
                close $f;
            }
        }
    } else {
        print $c "HTTP/1.0 400 BAD REQUEST\nContent-Type: text/plain\n\nBAD REQUEST\n";
    }
    close $c;
}
