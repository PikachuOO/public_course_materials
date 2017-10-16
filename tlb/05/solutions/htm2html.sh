#!/bin/sh

for file in *.htm
do
    new_file_name="$file"l
    if test -e "$new_file_name"
    then
        echo "$new_file_name exists"
        exit 1
    else
        mv "$file" "$new_file_name"
    fi
done
exit 0
