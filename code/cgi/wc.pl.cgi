#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Count words in a file.

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print <<eof;
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<title>Word Count</title>
</head>
<body>
eof

my $uploaded_file = param('filename');
if (defined $uploaded_file) {
    my ($lines, $words, $bytes);
    while ($line = <$uploaded_file>) {
        my @words = split /\s+/, $line;
        $words += @words;
        $bytes += length $line;
        $lines++;
    }
    printf "$uploaded_file: %d lines %d words %d bytes\n", $lines, $words, $bytes;
} 

print <<eof;
<form method="post" action="" enctype="multipart/form-data">
<input type="file" name="filename" value="Bitter.html">
<input type="submit" name="upload" value="Word Count File">
</form>
</body>
</html>
eof
