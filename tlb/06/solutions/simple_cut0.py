#!/usr/bin/python
import subprocess, sys
print()
subprocess.call(["cut","-c%s-%s"%(sys.argv[1:3]), sys.argv[3]])
