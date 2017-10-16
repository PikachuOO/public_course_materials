#!/usr/bin/perl -w

# return files in response to incoming http requests
# files with suffix .cgi executed and output returned
# only GET method supported
# assumes application/x-www-form-urlencoded data so CGI.pm won't work
# andrewt@cse.unsw.edu.au

# See http://search.cpan.org/dist/HTTP-Server-Simple/
# for a much  more general solution

use IO::Socket;
$server = IO::Socket::INET->new(LocalPort => 2041, ReuseAddr => 1, Listen => SOMAXCONN) or die;

print "Access this server at http://localhost:2041/\n\n";

while ($c = $server->accept()) {
    my $request = <$c>;
    if ($request =~ /^GET (.+) HTTP\/1.[01]\s*$/) {
        my $url = $1;
        $url =~ s/(^|\/)\.\.(\/|$)//g;
        if ($url =~ /^(.*\.cgi)(\?(.*))?$/) {
            my $cgi_script = "/home/cs2041/public_html/$1";
            $ENV{SCRIPT_URI} = $1;
            $ENV{QUERY_STRING} = $3 || '';
            $ENV{REQUEST_METHOD} = "GET";
            $ENV{REQUEST_URI} = $url;
            print $c "HTTP/1.0 200 OK\n";
            print $c `$cgi_script` if -x $cgi_script;
        } else {
            my $file = "/home/cs2041/public_html/$url";
            $file .= "/index.html" if -d $file;
            if (!-e $file) {
                print $c "HTTP/1.0 404 FILE NOT FOUND\nContent-Type: text/plain\n\nFile $file not found\n";
            } else {
                print $c "HTTP/1.0 200 OK\nContent-Type: text/html\n\n";
                open my $f, '<', $file or next;
                print $c (<$f>);
                close $f;
            }
        }
    } else {
        print $c "HTTP/1.0 400 BAD REQUEST\nContent-Type: text/plain\n\nBAD REQUEST\n";
    }
    close $c;
}
