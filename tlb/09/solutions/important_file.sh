#!/bin/sh

important_file=/home/cs2041/public_html/index.html

while ls $important_file >/dev/null 2>&1
do
        echo "all OK"
        sleep 1
done

echo "Panic $important_file gone"
