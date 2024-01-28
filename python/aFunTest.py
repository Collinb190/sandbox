#!/usr/bin/python3
"""
This module will define a function
"""
import math

def area_square():
    l = float(input("What is the length of the square?: "))
    w = float(input("What is the width of the square?: "))
    a = l * w
    
    print(a)

def area_circle():
    r = float(input("What is the radius(half) length?: "))
    a = math.pi * (r**2)

    print(f"{a:.2f}")

def get_area(shape):
    # this line takes away worrying about case sensitivity
    shape = shape.lower()

    if shape == "square":
        area_square()
    elif shape == "circle":
        area_circle()
    else:
        print("Must enter square or circle")

def god():
    shape_type = input("Get area for square or circle?: ")

    get_area(shape_type)

if __name__ == "__main__":
    god()