#!/usr/bin/python3
"""
This will decrypt messages
"""

x = input("Enter the message to be decoded\n")

numbers = x.split()
for i in range(0, len(numbers)):
    num = int(numbers[i])
    print(f"{chr(num)}", end="")
print()
