#!/usr/bin/python3
"""
Creates an alias
"""

# Enter the string to create an acrnym
x = input("Enter the string to create an acrnym\n")
# Remove the white space from the string
x = x.strip()
# Turn the string into a list
y = x.split() 
# Get the first char of each string in the list
a = ""
for word in y:
    a += word[0].capitalize()
print(a)
