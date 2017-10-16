#!/bin/sh
# http://cgi.cse.unsw.edu.au/~cs2041/13s2/lec/cgi/examples/typeahead/typeahead.sh/Hel
# http://localhost/~teachadmin/transcripts/typeahead.sh/Gam
echo "Content-Type: application/json"
echo
query=`echo $PATH_INFO|sed -r 's/^\///;s/[^a-zA-Z0-9, ]/.?/g;s/ +/ /'`

echo -n '['
egrep -i  -m 32 "\b$query" books.txt|
sed 's/"/ /g;s/^/"/;s/$/",/'|
tr -d '\n'|
sed 's/,$//'
echo ']'
