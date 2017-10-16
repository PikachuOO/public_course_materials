#!/usr/bin/perl -w

$important_file = "/home/cs2041/public_html/index.html";

while (!system "ls $important_file >/dev/null 2>&1") {
        system "echo \"all OK\"";
        system "sleep 1";
}
system "echo \"Panic $important_file gone\"";

