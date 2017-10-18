#!/usr/bin/python3
s = "The quick brown fox jumps over the lazy dog"
print(s)
a = s.split(" ")
print(a[5])
b = " ".join(a)
print(b)

s = "The quick brown fox 	jumps over the  lazy   dog"
a = s.split()
print(a[5])
b = " ".join(a)
print(b)


a = s.split(" ",5)
print(a[5])
b = " ".join(a)
print(b)

a = s.split(None,5)
print(a[5])
b = " ".join(a)
print(b)

s = "a*b+c|d^e&f(g[h{i?j.k$l"
a = s.split("*")
print(a[0])

a = s.split("+")
print(a[0])

a = s.split("|")
print(a[0])

a = s.split("^")
print(a[0])

a = s.split("&")
print(a[0])

a = s.split("(")
print(a[0])

a = s.split("[")
print(a[0])

a = s.split("{")
print(a[0])

a = s.split("?")
print(a[0])

a = s.split(".")
print(a[0])

a = s.split("$")
print(a[0])
