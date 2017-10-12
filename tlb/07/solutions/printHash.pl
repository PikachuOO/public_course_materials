#!/usr/bin/perl -w

sub printHash {
    my (%tab) = @_;
    my $n = 0;
    foreach $k (sort keys %tab) {
        print "[$k] => $tab{$k}\n";
        $n++;
    }
    return $n;
}

%h = ("David"=>"green", "Phil"=>"blue", "Andrew"=>"red", "John"=>"blue");

$nitems = printHash(%h);
print "#items = $nitems\n";
