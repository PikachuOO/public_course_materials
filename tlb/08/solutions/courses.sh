#!/bin/sh

for course in "$@"
do
    wget -q -O- http://www.timetable.unsw.edu.au/current/${course}KENS.html|
    egrep -oP "$course\d\d\d\d"|
    sort|
    uniq
done
