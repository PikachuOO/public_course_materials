#!/usr/bin/perl -w
# inspired by from www.cs.www.cs.rpi.edu/~hollingd/eiw.old/5-Perl/ex6.html

my $html_source = join "", <>;
my $modified_html = $html_source;
$modified_html =~ s/<\s*HEAD[^>]*>.*?<\s*\/HEAD[^>]*>//si;
$modified_html =~ s/<\s*\/?\s*(BODY|HTML)[^>]*>//gsi;

my ($title) = ($html_source =~ /.*<\s*TITLE[^>]*>(.*?)<\s*\/TITLE[^>]*>/si);
$title = "No title" if !defined $title;

$html_source =~ s/</\&lt;/g;
$html_source =~ s/>/\&gt;/g;

print <<eof;
<HTML>
<HEAD>
<TITLE>$title</TITLE>
</HEAD>
<BODY>
<H3 ALIGN=CENTER>HTML-VIEW of $title</H3>
<TABLE BORDER=1 BGCOLOR=WHEAT>
<TR><TD><PRE><FONT SIZE=SMALL>$html_source</FONT></PRE></TD><TD>$modified_html</TD></TR>
</TABLE>
</BODY>
</HTML>
eof
