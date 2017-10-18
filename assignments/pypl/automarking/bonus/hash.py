#!/usr/bin/python3
# stolen from 5116019
# tests translation of parameters to the def function, since it is very hard to determine the types
# without looking through the entire program for hints

def get_hash_value (hash, key):
	return hash[key]

my_hash = {'key':'value'}
my_key = 'key'
hash_value = get_hash_value(my_hash, my_key)

print(hash_value)
