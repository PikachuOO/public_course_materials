#!/usr/bin/perl -w

$function = $ARGV[0] or die "Usage: $0 <function-name>\n";

foreach $c_file (glob "*.c") {
    open my $cf, '<', $c_file or die "$0: can not open $c_file: $!\n";
    while ($line = <$cf>) {
        # remove single-line comments & strings (breaks if strings contain ")
        $line =~ s/\/\/.*//;
        $line =~ s/\/\*.*?\*\///;
        $line =~ s/".*?"//;
        # note use of \b (word boundary) to match function
        $line =~ /\b$function\s*\(/ or next;
        print "$c_file:$. function $function ";
        # if line is indented it should be a call to the function
        if ($line =~ /^\s/) {
            print "used\n";
        } elsif ($line =~ /;/) {
            print "declared\n";
        } else {
            print "defined\n";
        }
    }
    close $cf;
}