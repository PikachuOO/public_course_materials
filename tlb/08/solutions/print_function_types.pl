#!/usr/bin/perl -w

while ($line = <>) {
    $line =~ /^([a-zA-Z_].*)\((.*)\)/ or next;
    $function_start = $1;
    $parameter = $2;
    $function_type = $function_start;
    $function_type =~ s/\s*([a-zA-Z_]\w*)\s*$// or next;
    $function_name = $1;
    $parameter_type = $parameter;
    $parameter_type =~ s/\s*([a-zA-Z_]\w*)\s*$// or next;
    $parameter_name = $1;
    print "function type='$function_type'\n";
    print "function name='$function_name'\n";
    print "parameter type='$parameter_type'\n";
    print "parameter name='$parameter_name'\n";
}