#!/usr/bin/python3
import sys
from collections import OrderedDict
print(' '.join(OrderedDict.fromkeys(sys.argv[1:])));
