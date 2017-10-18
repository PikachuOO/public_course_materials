#!/bin/sh
TESTS_DIR=/home/cs2041/public_html/assignments/python2perl/tests
PATH=/home/give/stable/bin/:/usr/bin/:/bin:/usr/local/bin
export PATH
test -n "$DEBUG" && set -x 

rm -f  tmp.total
tests_passed=0
test_number=0
chmod 755 ./python2perl.pl
for test in $TESTS_DIR/*/*.py
do
	rm -f tmp.*
	test_number=`expr $test_number + 1`
	output=`echo $test|sed 's/\.py.*/.output/'`
	input=`echo $test|sed 's/\.py.*/.input/'`
	test -r $input  || input=$TESTS_DIR/default.input
	arguments_file=`echo $test|sed 's/\.py.*/.arguments/'`
	if test -r $arguments_file
	then
		arguments=`cat $arguments_file`
	else
		arguments=`cat $TESTS_DIR/default.arguments`
	fi
	if test ! -r $output
	then
#		echo  python $test $arguments '<'$input '>'$output 1>&2
		if python $test $arguments <$input >$output && test -s $output
		then
			chmod 444 $output
		else
			echo $test failed 2>&1
			exit
		fi
	fi
#	echo '#!/usr/bin/perl' >tmp.pl
	python=`basename $test`
	perl=`basename $test .py`.pl
	cp $test $python
	rm -f tmp.pl $perl
	if sed 1q ./python2perl.pl|grep '#!/usr/bin/python' >/dev/null
	then
		/home/andrewt/bin/timelim 5 python ./python2perl.pl $python 2>tmp.err >tmp.pl </dev/null
	else
		/home/andrewt/bin/timelim 5 perl -w ./python2perl.pl $python 2>tmp.err >tmp.pl </dev/null
	fi
	if grep -i 'limit exceeded' tmp.err >/dev/null
	then
		echo "--- Test $test_number failed ($test)"
		echo "Time limit of 30 seconds on translation exceeded."
		continue
	fi
	test -s $perl && cp  $perl tmp.pl
	if ! test -s tmp.pl
	then
		/home/andrewt/bin/timelim 5 perl -w ./python2perl.pl <$python 2>tmp.err >tmp.pl </dev/null
		if grep -i 'limit exceeded' tmp.err >/dev/null
		then
			echo "--- Test $test_number failed ($test)"
			echo "Time limit of 30 seconds on translation exceeded."
			continue
		fi
	fi
	if test ! -s tmp.pl
	then
		echo "--- Test $test_number failed ($test)"
		echo "No perl produced."
		sed 's/^/       /;20s/.*/.../;20q'  tmp.err
		echo
		continue
	fi
	timelimit=5;
#	echo  perl tmp.pl $arguments '<'$input 1>&2
	/home/andrewt/bin/timelim $timelimit perl tmp.pl $arguments <$input 2>tmp.err1 |
	dd 'bs=1' 'count=25000' 2>/dev/null|
	sed '1000q' >tmp.out
	perl -pi -e 's/\n*$/\n/ if eof' tmp.pl tmp.out tmp.err tmp.err1
	if grep -i 'limit exceeded' tmp.err1 >/dev/null
	then
		echo "--- Test $test_number failed ($test)"
		echo "Time limit of $timelimit seconds on Perl execution exceeded."
		echo "Your Perl was:"
		dd 'bs=1' 'count=2000' <tmp.pl 2>/dev/null|
		sed '/^#!/d;/^ *$/d;s/^/       /;50s/.*/.../;50q'
		sed 's/^/   /;20s/.*/.../;20q'  tmp.err
		echo
	elif test ! -s tmp.out
	then
		echo "--- Test $test_number failed ($test)"
		echo "No output produced by Perl when executed."
		echo "Your Perl was:"
		dd 'bs=1' 'count=2000' <tmp.pl 2>/dev/null|
		sed '/^#!/d;/^ *$/d;s/^/       /;50s/.*/.../;50q'
		sed 's/^/   /;20s/.*/.../;20q' tmp.err
		sed 's/^/   /;20s/.*/.../;20q' tmp.err1
		echo
	elif diff -Bw $output tmp.out >tmp.diff
	then
		echo "--- Test $test_number passed ($test)"
		tests_passed=`expr $tests_passed + 1`
	else
		echo "--- Test $test_number failed ($test)"
		echo "Your Perl was:"
		dd 'bs=1' 'count=2000' <tmp.pl 2>/dev/null|
		sed '/^#!/d;/^ *$/d;s/^/       /;50s/.*/.../;50q'
		sed 's/^/   /;20s/.*/.../;20q'  tmp.err
		echo "Your Perl when executed produced this output:"
		cat -v tmp.out|sed 's/^/       /;20s/.*/.../;20q'
		cat -v tmp.err1|sed 's/^/       /;20s/.*/.../;20q'  
		echo "The difference between your output and the correct output is:"
		sed 's/^/   /;20s/.*/.../;20q' tmp.diff
		echo
	fi
done
echo $tests_passed >tmp.total
echo
perl -pi -e 's/\n*$/\n/ if eof' *.py
for demo in 0 1 2 3 4 5 6 7 8 9
do
	file=demo$demo.py
	test -r $file || file=demo0$demo.py
	if test ! -r $file
	then
		echo "--- File $file not submitted"
		continue
	fi
	echo "--- Submitted demo file $file:"
	sed 's/^/   /;100s/.*/.../;100q' $file
	echo "Which is translated by the submission into this perl:"
	</dev/null /home/andrewt/bin/timelim 5 perl -w ./python2perl.pl $file  2>tmp.err1 |
	dd 'bs=1' 'count=25000' 2>/dev/null|
	sed 's/^/   /;;100s/.*/.../;100q'|
	perl -p -e 's/\n*$/\n/ if eof'
done
for test in 0 1 2 3 4 5 6 7 8 9
do
	file=test$test.py
	test -r $file || file=test0$test.py
	if test ! -r $file
	then
		echo "--- Test $file not submitted"
		continue
	fi
	echo "--- Submitted test file $file:"
	sed 's/^/   /;100s/.*/.../;100q' $file
done
exit 0
