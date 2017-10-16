#!/usr/bin/perl -w

# Build hash table of phone numbers, where keys
# are "person:phone-type" strings

open my $phones, '<', "phones.txt" or die "Can not open phones.txt:$!\n";

while ($line = <$phones>) {
    chomp $line;
    my ($id,$type,$number) = split /,/, $line;
    $phones{"$id:$type"} = $number;
}

close $phones;

# Iterate through People, displaying values
open my $people, '<', "people.txt" or die "Can not open people.txt:$!\n";

while ($line = <$people>) {
    chomp $line;
    my ($id,$name,$street,$suburb) = split /,/, $line;
    print "$name\n$street, $suburb\nPhones: ";
    my $nphones = 0;
    foreach $type ('mobile', 'home', 'work') {
        my $key = "$id:$type";
        if (defined($phones{$key})) {
            $num = $phones{$key};
            print ", " if ($nphones++ > 0);
            print "$num ($type)";
        }
    }
    print "?" if ($nphones == 0);
    print "\n\n";
}

close $people;