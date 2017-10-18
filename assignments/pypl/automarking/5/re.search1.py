#!/usr/bin/python3
import re
line = 'The quick brown fox jumped over the lazy dog'
if re.search('The', line): print('a')
if re.search('quick', line): print('b')
if re.search('dog', line): print('c')
