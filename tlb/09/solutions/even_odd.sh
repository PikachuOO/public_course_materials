#!/bin/bash
number=0
while test $number -ge 0
do
	echo -n "Enter number: "
    read number
    if  test $number -ge 0
    then
        if  test `expr $number % 2` -eq 0
        then
            echo "$number is even"
        else
            echo "$number is odd"
        fi
    fi
done
echo "Bye"
