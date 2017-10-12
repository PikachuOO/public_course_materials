#!/bin/sh
# exits with a status of 0  if the current time is between 9am & 5pm
# otherwise exit with a status 1
#
# date format looks like this Sun Mar 18 12:57:08 EST 2012

current_hour=`date|cut -d\  -f4|cut -d: -f1`
if test $current_hour -ge 9 -a $current_hour -lt 17
then
    exit 0
else
    exit 1
fi
