#!/usr/bin/python3
a = 1
if a:
    for i in range(10):
        if i % 2:
            continue
        elif i < 3:
            continue
        elif i > 8:
            break
        else:
            print(i)

