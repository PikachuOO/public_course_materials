#!/usr/bin/python3
# stolen from 5116019
# tests translation of parameters to the def function, since it is very hard to determine the types
# without looking through the entire program for hints

# tests having two re.subs on one line since perl can only do one sub without
# the non-destructive modifier r

import re

str = re.sub('e', 'E', re.sub('o', 'O', "hello"))
print (str)
