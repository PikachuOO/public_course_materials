#!/usr/bin/perl -w

sub hashToHTML {
    my (%tab) = @_;
    my $html = "";

    $html = "<table border=\"1\" cellpadding=\"5\">\n".
        "<tr><th> Key </th><th> Value </th></tr>\n";

    foreach $k (sort keys %tab) {
        $html .= "<tr><td> $k </td><td> $tab{$k} </td></tr>\n";
    }
    $html .= "</table>\n";
    return $html;
}

%h = ("David"=>"green", "Phil"=>"blue", "Andrew"=>"red", "John"=>"blue");

print hashToHTML(%h);
exit;
