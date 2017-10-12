#!/usr/bin/perl -w

if (@ARGV == 0) { # no args, read from stdin
    print reverse <STDIN>;
}
else {
    foreach $file (@ARGV) {
        open my $input, '<', $file or die "$file:can not open: $!\n";
        print reverse <$input>;
        close $input;
    }
}