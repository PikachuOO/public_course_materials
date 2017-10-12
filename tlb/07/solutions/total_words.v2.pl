#!/usr/bin/perl -w
$count = 0;
while (<STDIN>) {
    foreach (/[a-z]+/ig) {
        $count++;
    }
}
print "$count words\n"