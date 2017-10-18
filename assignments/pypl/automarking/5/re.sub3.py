#!/usr/bin/python3
import re
str = 'The quick brown fox jumped over the lazy dog'
print(str)
str = re.sub('fox', 'wolf', str)
print(str)
str = re.sub('dog', 'cat', str)
print(str)
