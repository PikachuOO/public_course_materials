#!/bin/sh

for c_file in "$@"
do
	for include_file in `grep '^#include *"' "$c_file"|sed 's/" *$//;s/.*"//'`
	do
		if test ! -r "$include_file"
		then
			echo "$include_file included into $c_file does not exist"
		fi
	done
done