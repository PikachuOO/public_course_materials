#!/bin/sh

grep COMP[29]041 "$1"|
cut -d\| -f3|
cut -d, -f2|
cut -d\  -f2|
sort|
uniq -c|
sort -nr|
head -1|
sed 's/.* //'
