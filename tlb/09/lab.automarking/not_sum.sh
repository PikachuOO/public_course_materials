#!/bin/bash

# sum the integers $start .. $finish

start=1
finish=10
sum=0

counter=2
while ((finish >= counter))
do
    sum=$((counter + sum ))
    counter=$((counter + 2))
done

echo Sum of the integers $start .. $finish = $sum
