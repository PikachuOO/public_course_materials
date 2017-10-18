#!/usr/bin/python3
# stolen from 3470062
# Testing the handling of strings and print statements
string = "$ARGV[0]"
print(string)
print()
print("string")
print("")
print("$string")
print('')
print(r"string\n")
print("\n")
print('print(print("test"))')
print(r"$string")
print(r"\n")
print("\"\"")
print('\"\"')
print('""')
print("test'test'test")
print('\'\'')
print(", $ARGV[0], \n, ")
print(', $ARGV[0], "\n", ')
print(r', $ARGV[0], "\n", ')
