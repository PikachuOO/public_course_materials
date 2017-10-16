#!/usr/bin/perl
# Simple CGI script written by andrewt@cse.unsw.edu.au

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print header, start_html('My Status'), h2('Status Summary');
warningsToBrowser(1);

$data_directory = "./status_data/";
-d $data_directory or mkdir $data_directory or die "Cannot create $data_directory: $!\n";

if (param('new_status')) {
    my $user = param('user');
    $user =~ s/\W//;
    my $correct_password;
    open my $p, '<', "status_passwords" or die;
    while (<$p>) {
        print pre("user $user = xxx$_xxx");
        last if ($correct_password) = /$user:(.*)$/;
    }
    close $p;
    print "Correct='$correct_password'\n";
    if (defined $correct_password && $correct_password eq param('password')) {
        open my $s, '>', "$data_directory/$user" or die;
        print $s param('new_status');
        close $s;
        print "Status for $user updated\n",p;
    } else {
        print "Error: could not update status for $user\n",p;
    }
}

foreach $status_file (glob "$data_directory/*") {
    my ($user) = $status_file =~ /\/([^\/]*)$/;
    open my $f, '<', $status_file or next;
    my $user_status = join '', <$f>;
    close $f;
    print "<li> $user: $user_status\n";
}
print   hr,
        start_form,
        p, 'Username: ', textfield('user'),
        p, 'Password: ', textfield('password'),
        p, 'New status: ', textfield('new_status'),
        p, submit('Update status'),
        end_form,
        end_html;
exit 0;

