#!/usr/bin/perl -w
$option_day_time = 0;
$option_table = 0;
$base_url = "http://timetable.unsw.edu.au/current";
$debug = 0;
foreach $arg (@ARGV) {
    if ($arg eq "-d") {
        $option_day_time = 1;
    } elsif ($arg eq "-t") {
        $option_table = 1;
    } elsif ($arg eq "--debug") {
        $debug = 1;
    } else {
        push @courses, $arg;
    }
}
foreach $course (@courses) {
    my %lectures_seen;
    open my $f, '-|', "wget -q -O- $base_url/$course.html" or die "Can not fetch web page for $course: $!";
    while ($line = <$f>) {
        next if $line !~ /href.*>Lecture/;
        print "found line: '$line'\n" if $debug;
        my $session = "";
        $line = <$f>;
        $session = $& if $line =~ /[A-Z][0-9]/;
        <$f> foreach 1..4; # skip 5 lines
        $line = <$f>;
        chomp $line;
        print "raw line = '$line'\n" if $debug;
        $line =~ s/<.*?>//g;
        $line =~ s/^\s*//g;
        $line =~ s/\s*$//g;

        next if !$line;
        next if $lectures_seen{$line}++;

        print "$course: $session $line\n" if !$option_day_time && !$option_table;

        foreach $lecture (split /\), /, $line) {
            print "lecture='$lecture'\n" if $debug;
            my @days = $lecture =~ /\b([a-z]{3})\b/gi ;
            print "\@days='@days'\n" if $debug;

            my ($start_hour,$finish_hour,$finish_minute) = $lecture =~ /(\d\d):\d\d - (\d\d):(\d\d)/ or next;
            $finish_hour++ if $finish_minute ne "00";
            print "start_hour=$start_hour finish_hour=$finish_hour\n" if $debug;

            foreach $day (@days) {
                foreach $time ($start_hour..$finish_hour-1) {
                    if (!$lecture{$session}{$day}{$time}{$course}++ and $option_day_time) {
                        print "$session $course $day $time\n";
                    }
                }
            }
        }
    }
    close $f;
}

if ($option_table) {
    foreach $session (sort keys %lecture) {
        my @days =qw/Mon Tue Wed Thu Fri/;
        my $width = 6;
        printf "%-${width}s", $session;
        printf "%${width}s",$_ foreach @days;
        print "\n";
        foreach $time (9..20) {
            printf "%02d:00", $time;
            foreach $day (@days) {
                my $n_lectures =  keys %{$lecture{$session}{$day}{$time}};
                printf "%${width}s", $n_lectures || "";
            }
            print "\n";
        }
    }
}