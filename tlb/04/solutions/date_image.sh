#!/bin/sh

for image_file in "$@"
do
    last_modify_time=`ls -l "$image_file"|cut -d\  -f5-|sed 's/^ *//'|cut -d\  -f2-4`
    temporary_file="$image_file.tmp.$$"
    if test -e "$temporary_file"
    then
        echo "$temporary_file" already exists
        exit 1
    fi
    convert -gravity south -pointsize 36 -draw "text 0,10 '$last_modify_time'" "$image_file" "$temporary_file" &&
    touch -r "$image_file" "$temporary_file" &&  # preserve modification time (challenge question)
    mv "$temporary_file" "$image_file"
done