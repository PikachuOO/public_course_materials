#!/usr/bin/python3
# stolen from 5059649
# Testing string split and join
string = "1,2,3"
comma = ","
arr = "1,2,3".split(comma)
print(' '.join(arr))
arr = string.split(r",",maxsplit=1)
print(' '.join(arr))
string = "1 2 3"
arr = string.split()
print('-'.join(arr))
arr = string.split(maxsplit=1)
print('-'.join(arr))

