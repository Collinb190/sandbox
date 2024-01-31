#!/usr/bin/python3
"""
This will generate an acronym
"""
if __name__ == "__main__":
    # Get the input
    x = input("Enter your string\n")
    # Remove any whitespace
    x = x.strip()
    # Convert the string into a list
    y = list(x)
    z = ""
    for word in y:
        z += word[0]
    print(z)
