#!/usr/bin/python3
"""
secret message
ord - to get number value
chr - to get char value
"""

x = input("Enter a string to encode to a secret message\n")

for char in x:
    print(f"{ord(char)}", end=" ")
print()

