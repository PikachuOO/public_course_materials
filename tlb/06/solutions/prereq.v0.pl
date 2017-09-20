#!/usr/bin/perl -w

$year = 2016;
$url_base = "http://www.handbook.unsw.edu.au/";
$url_ugrad = "$url_base/undergraduate/courses/$year";
$url_pgrad = "$url_base/postgraduate/courses/$year";

foreach $course (@ARGV) {
    open my $f, '-|', "wget -q -O- $url_ugrad/$course.html $url_pgrad/$course.html" or die;
    while ($line = <$f>) {
        # look for pre-requisite line handling varying format used  in handbook pages
        if ($line =~ /pre.?(requisite)?(.?:|\s+[A-Z]{4}\d{4})/i) {
            $line = uc $line;
            $line =~ s/<[^>]*>/ /g;
            $line =~ s/EXCLU.*/ /i;
            my @courses = $line =~ /([A-Z]{4}\d{4})/g;
            push @prereqs, @courses;
        }
    }
    close $f;
}
foreach $course (sort @prereqs) {
    print "$course\n";
}
