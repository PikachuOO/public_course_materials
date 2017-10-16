#!/bin/sh
# Write the sequence of integers specified by command-line arguments
# Check and handle command-line args

case $# in
1) lo=1   hi=$1  inc=1 ;;
2) lo=$1  hi=$2  inc=1 ;;
3) lo=$1  hi=$3  inc=`expr $2 - $1` ;;
*) cat <<EOI
Usage:
  $0 hi         ... prints numbers in range 1..hi
  $0 lo hi      ... prints numbers in range lo..hi
  $0 lo 2nd hi  ... prints numbers lo,2nd,..hi
                    (using difference between lo and
                     2nd as the increment)
EOI
   exit 1 ;;
esac

# Generate integer sequence

i=$lo
while test $i -le $hi
do
    echo $i
    i=`expr $i + $inc`
done
