#!/usr/bin/perl -w
# Simple CGI script written by andrewt@cse.unsw.edu.au
# to demonstrate a possible CGI security hole

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print <<eof;
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<title>Insecure 2041 admin script</title>
</head>
<body>
eof

warningsToBrowser(1);

# insecure: user may set this parameter directly
# For example using using this URL:
# http://www.cse.unsw.edu.au/code/cgi/admin_script.cgi?password_checked=1&student_number=5555555&new_mark=100

if (param('password_checked')) {
    if (param('student_number') && param('new_mark')) {
        mark_changed_screen();
    } else {
        change_mark_screen()
    }
} elsif (defined param('login') && defined param('password')) {
    if (authenticate_password()) {
        param('password_checked', 1);
        change_mark_screen();
    } else {
        wrong_password_screen();
    }
} else {
    login_screen();
}

exit 0;

sub login_screen {
    print <<eof
<form action="">
Enter login: <input type="textfield" name="login">
<br>
Enter password: <input type="password" name="password">
<br>
<input type="submit" value="Login">
</form>
</body>
</html>  
eof
}

sub wrong_password_screen {
    print "Login or password incorrect.\n<p>\n";
    login_screen();
}


sub authenticate_password {
    my $login = param('login');
    my $password = param('password');
    return $login && $password && $login eq "andrewt" && $password eq "secret";
}

sub change_mark_screen {
    print <<eof
<form action="">
Enter 2041 student number: <input type="textfield" name="student_number">
<br>
Enter new mark: <input type="textfield" name="new_mark">
<br>
<input type="submit" value="Change mark">
<input type="hidden" name="password_checked" value="1">
</form>
</body>
</html>  
eof
}

sub mark_changed_screen {
    my $student_number = param('student_number');
    my $new_mark = param('new_mark');
    print  "Mark for $student_number set to $new_mark\n<p>\n";
    change_mark_screen();
}

