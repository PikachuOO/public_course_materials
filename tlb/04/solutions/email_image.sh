#!/bin/sh

for png_file in "$@"
do
    display "$png_file"
    echo -n "Address to e-mail this image to? "
    read address
    if test -n "$address"
    then
        echo -n "Message to accompany image? "
        read message
        echo "$message"| mutt -s 'image' -a "$png_file" -e 'set copy=no' -- "$address"
        echo "$png_file sent to $address"
    else
        echo "No email sent"
    fi
done
