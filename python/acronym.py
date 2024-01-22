#!/usr/bin/python3
"""
Creates an acronym
"""

# Get string/ Remove whitespace/ String to list/ Hold acronym
x = input("Enter the string to create an acronym\n")
x = x.strip()
y = x.split()
a = ""

# Get the first char of each string in the list
for word in y:
    a += word[0].capitalize()
print(a)
