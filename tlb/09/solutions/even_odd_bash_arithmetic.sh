#!/bin/bash
number=0
while ((number >= 0))
do
    echo -n "Enter number: "
    read number
    if ((number >= 0))
    then
        if ((number % 2 == 0))
        then
            echo "$number is even"
        else
            echo "$number is odd"
        fi
    fi
done
echo "Bye"
