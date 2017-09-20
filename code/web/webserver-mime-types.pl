#!/usr/bin/perl -w

# return files in response to incoming http requests to port 2041,
# determine appropriate mime type using /etc/mime.types
# andrewt@cse.unsw.edu.au

use IO::Socket;

print "Access this server at http://localhost:2041/\n\n";

open my $mt, '<', "/etc/mime.types" or die "Can not open /etc/mime.types: $!\n";
while ($line = <$mt>) {
    $line =~ s/#.*//;
    my ($mime_type, @extensions) = split /\s+/, $line;
    foreach $extension (@extensions) {
        $mime_type{$extension} = $mime_type;
    }
}
close $mt;
while (1) {
    $server = IO::Socket::INET->new(LocalPort => 2041, ReuseAddr => 1, Listen => SOMAXCONN) or die;
    while ($c = $server->accept()) {
        print "waiting for connection";
        my $request = <$c>;
        last if !$request;
        printf "Connection from %s, request: $request", $c->peerhost;
        my $content_type = "text/plain";
        my $status_line = "400 BAD REQUEST";
        my $content = "";

        if (my ($url) = $request =~ /^GET (.+) HTTP\/1.[01]\s*$/) {
            # remove any occurences of .. from pathname to prevent access outside 2041 directory
            $url =~ s/(^|\/)\.\.(\/|$)//g;
            my $file = "/home/cs2041/public_html/$url";
            $file .= "/index.html" if -d $file;

            print "$file requested\n";
            if (open my $f, '<', $file) {
                my ($extension) = $file =~ /\.(\w+)$/;
                $status_line = "200 OK";
                $content_type = $mime_type{$extension} if $extension && $mime_type{$extension};
                $content = join "", <$f>;
            } else {
                $status_line = "404 FILE NOT FOUND";
                $content = "File $file not found\n";
            }
        }

        my $header = sprintf "HTTP/1.0 $status_line\nContent-Type: $content_type\nContent-Length: %d\n\n", length($content);
        print "Sending this header:\n", $header;

        print $c $header, $content;;
        close $c;
    }
}