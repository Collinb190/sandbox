#!/usr/bin/python3
"""
This module is for testing
"""

import random
num = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess a number 1-10: "))
        if guess == num:
            print("You got it!")
            break
        elif guess <= 0 or guess > 10:
            print("Enter integer between 1-10")
        else:
            print("Try again!")
    except ValueError:
        print("Must enter a value 1-10")
    except KeyboardInterrupt:
        print("Exiting the program")
        break
    except EOFError:
        print("End of the file reached...exiting.")
        break
