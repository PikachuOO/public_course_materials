#!/usr/bin/perl -w
while (<STDIN>) {
    tr/0-9/<<<<<5>>>>/;
    print;
}
