#!/usr/bin/perl
# CGI script written by andrewt@cse.unsw.edu.au
# See match.html

use CGI qw/:all/;
print header;
if (param('string') =~ param('regex')) {
    print b('Match succeeded, this substring matched: ');
    print tt(escapeHTML($&));
} else {
    print b('Match failed');
}
