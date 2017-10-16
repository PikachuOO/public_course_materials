#!/usr/bin/perl -w
$number = 0;
while ($number >= 0) {
	print "Enter number: ";
    $number = <STDIN>;
    chomp $number;
    if ($number >= 0) {
        if ($number % 2 == 0) {
            print "$number is even\n";
        } else {
            print "$number is odd\n";
        }
    }
}
print "Bye\n";
