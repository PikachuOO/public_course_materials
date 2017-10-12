#!/bin/sh

for album_pathname in "$@"
do
    album=`basename "$album_pathname"`
    year=`echo "$album"|sed 's/.* //'`

    for mp3_pathname in "$album_pathname"/*.mp3
    do
        mp3_filename=`basename "$mp3_pathname" .mp3`
        # assume ' - ' doesn't occur in artist or album
        track=`echo "$mp3_filename"|sed 's/ - .*//'`
        title=`echo "$mp3_filename"|sed 's/^[0-9]* - //;s/ - .*//'`
        artist=`echo "$mp3_filename"|sed 's/.* - //'`
        id3 -t "$title" -T "$track" -a "$artist" -A "$album" -y "$year" "$mp3_pathname" >/dev/null
    done
done
