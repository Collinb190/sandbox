#!/usr/bin/python3
"""
This module will define a function
"""


def aFun():
    """
    function
    """
    math = input("Enter the problem:\n")
    math = math.strip()
    myList = math.split()
    x = int(myList[-1]) - int(myList[2])
    print(x)

def bFun(prob):
    """
    function
    """
    prob = prob.strip()
    myList = prob.split()
    x = int(myList[-1]) - int(myList[2])
    return str(x)

prob = input("Enter your problem:\n")
x = bFun(prob)
print("x = " + x)
