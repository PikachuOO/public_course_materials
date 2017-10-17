#!/usr/bin/perl -w

$max_lines = 10;

if (@ARGV > 0 && $ARGV[0] =~ /-([0-9]+)/) {
    $max_lines = $1;
    shift @ARGV;
}

if (@ARGV == 0) {
    @lines = <>;
    $first = @lines - $max_lines;
    $first = 0 if $first < 0;
    print @lines[$first..$#lines];
} else {
    $show_file_names = @ARGV > 1;
    foreach $file (@ARGV) {
        open my $f, '<', $file or die "$0: can't open $file\n";
        print "==> $file <==\n" if $show_file_names;
        @lines = <$f>;
        $first = @lines - $max_lines;
        $first = 0 if $first < 0;
        print @lines[$first..$#lines];
        close $f;
    }
}
