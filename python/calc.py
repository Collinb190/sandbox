#!/usr/bin/python3
"""This module will act as a simple calculator"""


# create a calc function that will take in the values obtained
def calc(a, b, o):
    """This will calculate based on the values and operator
    Args:
        a: the fist value
        b: the second value
        o: the result of the calculation
    
    Returns:
        The calculated value from the operation
    """
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a / b
    else:
        raise ValueError("o must be a valid operator")

def main():
    """This will be the main calc method"""
    a = float(input("Enter value a\n"))
    b = float(input("Enter value b\n"))
    o = input("Enter the operation to preform\n")

    result = calc(a, b, o)
    print(f"{a} {o} {b} = {result}")
if __name__ == "__main__":
    main()
