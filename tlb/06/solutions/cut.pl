#!/usr/bin/perl -w

$delim = "\t";
if ($ARGV[0] =~ /-d./) {
    ($delim = $ARGV[0]) =~ s/-d//;
    shift;
}
if ($ARGV[0] =~ /-f*/) {
    ($flist = $ARGV[0]) =~ s/-f//;
    if ($flist eq "")
        { shift; $flist = $ARGV[0]; }
    @fields = split(/,/,$flist);
    shift;
}
while (<>) {
    chomp;
    @words = split /$delim/;
    @outs = ();
    $nf = $#words;
    foreach $f (@fields) {
        push @outs, $words[$f-1] if ($f <= $nf+1);
    }
    print join($delim,@outs)."\n";
}
