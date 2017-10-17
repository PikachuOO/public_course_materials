#!/bin/bash

# calculate powers of 2 by repeated addition

variable2=10
variable1=3
while ((variable2 < 20))
do
    variable1=$((variable1 + variable1))
    echo $variable2 $variable1
    variable2=$((variable2 + 1))
done
