#!/usr/bin/python3
"""
This will decrypt messages
"""

x = input("Enter the message to be decoded\n")

for num in x:
    num = int(num)
    print(f"{chr(num)}", end=" ")
print()

