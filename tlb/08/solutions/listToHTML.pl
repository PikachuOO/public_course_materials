#!/usr/bin/perl -w

sub listToHTML(@) {
    my (@list) = @_;
    return "" if !@list;
    return "<ul>\n<li>".join("\n<li>", @list)."\n</ul>\n";
}
print listToHTML(@ARGV);
