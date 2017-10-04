#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# Allow users to change a file

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('Editing A File');
warningsToBrowser(1);

$filename = "editfile.data";
$file_content = param('content');

if (param('Save') && defined $file_content) {
    if (open FILE, '>', $filename) {
    	print FILE $file_content;
    	close FILE;
    	print "File saved\n", end_html;
    } else {
    	print "Save failed\n", end_html;
    }
    exit 0;
}

if (!defined $file_content && open F, '<', $filename) {
	$file_content = join "", <F>;
	param('content', $file_content);
}

print   start_form, "\n",
        textarea(-name=>'content', -rows=>10,-cols=>60), "\n",
        p, submit('Save'), "\n",
        end_form, "\n",
        end_html;
