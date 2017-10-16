#!/bin/sh
# list the files included by the C sources files included as arguments
if test $# = 0
then
    echo "Usage: $0 <files>"
    exit 1
fi

egrep '^#include' "$@"|  # find '#include lines
sed 's/[">][^">]*$//'|  # remove the last '"' or '>' and anything after it
sed 's/^.*["<]//'|      # remove the last '"' or '>' and anything before it
sort|                   # sort the file names
uniq                    # remove any duplicates
