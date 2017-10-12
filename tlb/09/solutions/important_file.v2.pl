#!/usr/bin/perl -w

$important_file = "/home/cs2041/public_html/index.html";

while (-e $important_file) {
        print "all OK\n";
        sleep 1;
}
print "Panic $important_file gone\n";

