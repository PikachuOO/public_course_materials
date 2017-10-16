#!/usr/bin/perl -w
if ($ARGV[0] =~ /-[0-9]+/) {
    $max = shift @ARGV;
    $max =~ s/-//;
} else {
    $max = 10;
}
# default is stdin if no files specified
$ARGV[0] = "-" if @ARGV == 0;
foreach $file (@ARGV) {
    open my $input, '<', $file or die "$file: can not open: $!\n";
    print "==> $file <==\n";
    @lines = <$input>;
    print @lines[0..$max-1];
    close $input;
}