#!/usr/bin/perl -w
# using the implicit variable $_
while (<STDIN>) {
    s/[0-4]/</g;
    s/[6-9]/>/g;
    print;
}
