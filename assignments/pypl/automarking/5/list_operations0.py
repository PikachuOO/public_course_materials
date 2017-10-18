#!/usr/bin/python3
# stolen from 5059649
li = []
li.append("1")    # li is now [1]
li.append("2")    # li is now [1, 2]
li.append("4")    # li is now [1, 2, 4]
li.append("3")    # li is now [1, 2, 4, 3]
print(' '.join(li))
li.pop()
print(' '.join(li))
li.append("3")
li.pop(2)
print(' '.join(li))
print(li[0])
print(li[-1])
print(' '.join(li[1:3]))
print(' '.join(li[1:]))
print(' '.join(li[:3]))
print(' '.join(li[:]))
