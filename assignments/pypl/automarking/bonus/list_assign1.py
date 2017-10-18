#!/usr/bin/python3
test = "hello:world:something:orother"
h, w, rest = test.split(':', 2)
print("h=", h)
print("w=", w)
print("rest=", rest)
