#!/usr/bin/python3
# stolen from 5098910
# I start out with 3 spaces
if 1 < 2:
   str1 = "Hello"
   str2 = "Hello world"
   str3 = "HELLO WORLD"
   if (str1 < str2):
    # then change to tab with width 3 for inner levels
    print("shorter words are lesser", end = "----------\n")
   else:
    print("longer words are greater", end = "10202030303\n")

   print("Uh oh blank line")
   if (str1 == str2 or 1 == 1):
    print("one of these are true", end="as;dlkfjdksafsdfa\n")
    if (str3 > str2):
        print("Capitals are greater")
    else:
        print("Lower case is greater or equal!", end = "31498134")
        # let's hope you put closing braces in!
        # most people don't fix indents for comments, let's hope your don't need that
        # to put closing braces in
