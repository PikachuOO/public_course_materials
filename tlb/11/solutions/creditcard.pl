#!/usr/bin/perl -w
# written by andrewt@cse.unsw.edu.au as a COMP2041 programming example
# validate a credit card number by calculating its
# checksum using Luhn's formula (https://en.wikipedia.org/wiki/Luhn_algorithm)

sub luhn_checksum {
    my ($number) = @_;
    my $checksum = 0;
    my @digits = reverse(split //, $number);
    foreach $index (0..$#digits) {
        my $digit = $digits[$index];
        my $multiplier = 1 + $index % 2;
        my $check_digit = int($digit) * $multiplier;
        if ($check_digit > 9) {
            $check_digit -= 9;
        }
        $checksum += $check_digit;
    }
    return $checksum;
}

sub validate {
    my ($credit_card) = @_;
    my $number = $credit_card;
    $number =~ s/\D//g;
    if (length $number != 16) {
        return  "invalid - does not contain exactly 16 digits";
    } elsif (luhn_checksum($number) % 10 == 0) {
        return "valid";
    } else {
        return "invalid";
    }
}

foreach $credit_card (@ARGV) {
    print "$credit_card is ", validate($credit_card), "\n";
}
