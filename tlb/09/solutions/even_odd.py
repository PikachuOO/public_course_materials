#!/usr/bin/python3
number = 0
while number >= 0:
    number = int(input("Enter number: "))
    if number >= 0:
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "odd")
print("Bye")
