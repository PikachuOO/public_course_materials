#!/bin/sh
# Write the sequence of integers specified by command-line arguments
# The bash-specific syntax ((..)) is used for arithmetic

if (($# == 1))
then
    lo=1
    hi=$1
    inc=1
elif (($# == 2))
then
    lo=$1
    hi=$2
    inc=1
elif (($# == 3))
then
    lo=$1
    hi=$3
    inc=$(($2 - $1))
else
    cat <<EOI
Usage:
  $0 hi         ... prints numbers in range 1..hi
  $0 lo hi      ... prints numbers in range lo..hi
  $0 lo 2nd hi  ... prints numbers lo,2nd,..hi
                    (using difference between lo and
                     2nd as the increment)
EOI
   exit 1
fi

i=$lo
while (($i <= $hi))
do
    echo $i
    i=$(($i + $inc))
done
