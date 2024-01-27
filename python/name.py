#!/usr/bin/python3
"""
This module will define the name function.
"""


def name(first="", last=""):
    """
    This will print the first and last name of a person.
    
    Args:
        first (str): The first name of the person.
        last (str): The last name of the person.
    Returns:
        n (str): The full name.
    """
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    n = first + " " + last
    print(f"Hello {n}! Welcome to the machine!")

if __name__ == "__main__":
    name()