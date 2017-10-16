#!/usr/bin/python
import fileinput, re, sys, collections
ncorrect = collections.defaultdict(int)
total = collections.defaultdict(float)
for line in fileinput.input():
    (sid,ex,tests,warns) = line.split()
    if tests == '5':
        mark = 10
        ncorrect[sid] += 1
    else:
        mark = int(tests)/2.0
    if int(warns) > 0:
        mark = max(0, mark - 2)
    total[sid] += mark
for sid in sorted(total.keys()):
    if ncorrect[sid] >= 2:
        passfail = "PASS"
    else:
        passfail = "FAIL"
    print("%s %4.1f %s" % (sid, total[sid], passfail))
