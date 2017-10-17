#!/bin/sh

input=/tmp/shuffle_test0$$
output=/tmp/shuffle_test1$$
sorted_output=/tmp/shuffle_test2$$
all_output=/tmp/shuffle_test3$$

number_of_lines=4
number_of_test_runs=256

# create an input file with 1 integer per line in sorted order
# and calculate how many permutations are possible
i=1
factorial=1
while test $i -le $number_of_lines
do
    echo $i
    factorial=$(($factorial * $i))
    i=$(($i + 1))
done >$input

run=1
while test $run -le $number_of_test_runs
do
    ./shuffle.pl <$input >$output
    sort -n $output >$sorted_output

    # after sorting output should be identical to input
    if diff $sorted_output $input >/dev/null
    then
        # append result of this execution to $all_output as a single line
        echo `cat $output` >>$all_output
    else
        echo Testing failed, input was:
        cat $input
        echo Testing failed, output was:
        cat $output
        exit 1
    fi
    run=$(($run + 1))
done

n_different_outputs=`sort $all_output|uniq|wc -l`
if test $n_different_outputs -eq $factorial
then
    echo All possible outputs produced
    exit 0
else
    echo In $number_of_test_runs executions only $n_different_outputs of $factorial outputs produced
    exit 1
fi

rm -f $input $output $sorted_output $all_output