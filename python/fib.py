#!/usr/bin/python3
"""
This module will define the fib function.
"""


def fib(n):
    """
    Generates a Fibonacci sequence containing the first n terms.

    Args:
        n (int): The amount of terms.
    Returns:
        seq (list): The Fibonacci sequence.
    """
    myList = [0, 1]

    for i in range(2, n):
        myList.append(myList[i - 1] + myList[i - 2])
    return myList

if __name__ == "__main__":
    print(fib(8))