#!/usr/bin/python3
"""
secret message encoder and decoder!
ord - to get number value
chr - to get char value
"""

def encode():
    """This function will encode your message."""

    x = input("Enter a string to encode to a secret message\n")

    for char in x:
        print(f"{ord(char)}", end=" ")
    print()

def decode():
    """This function will encode your message."""

    x = input("Enter the message to be decoded\n")

    numbers = x.split()
    for i in range(0, len(numbers)):
        num = int(numbers[i])
        print(f"{chr(num)}", end="")
    print()

def main():
    while True:
        message = input("Would you like to encode or decode?\n")
        if message == "encode":
            encode()
            break
        elif message == "decode":
            decode()
            break
        else:
            print("must enter decode or encode")

if __name__ == "__main__":
    main()
