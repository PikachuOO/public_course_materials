#!/usr/bin/python3
a = list(range(10))
for i in sorted(a):
	print(i)

b = {"a":1,"b":2,"c":3}
c = "b"

if "a" in b:
	print("True")
else:
	print("False")

if "d" in b:
	print("True")
else:
	print("False")
	
if "a" not in b:
	print("True")
else:
	print("False")

if "d" not in b:
	print("True")
else:
	print("False")
	
if c in b:
	print("True")
else:
	print("False")

if c not in b:
	print("True")
else:
	print("False")
