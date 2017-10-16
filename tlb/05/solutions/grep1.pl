#!/usr/bin/perl -w
# - grep(/pattern/,@array) returns array containing
#   just elements that match the pattern

$pattern = shift @ARGV;
print grep(/$pattern/, <>);

# behaves like ... cat f1 f2 f3 .. | grep pattern
# not the same as ... grep pattern f1 f2 f3 ..

