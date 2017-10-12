#!/bin/sh
# exits with a status of 0  if the current time is between 9am & 5pm
# otherwise exit with a status 1
# date output looks like this 'Sun Mar 18 12:57:08 EST 2012'
# relies on the exit status being the exit status of last command
# when there isn't an explicit exit

current_hour=`date|cut -d\  -f4|cut -d: -f1`
test $current_hour -ge 9 -a $current_hour -lt 17
