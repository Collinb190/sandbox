#!/usr/bin/python3
height = eval(input("what is the height?"))
spaces = height - 1
stumpSpace = height - 1
hashes = 1
while height != 0:
    for i in range(spaces):
        print(" ", end="")
    for i in range(hashes):
        print("#", end="")
    print()
    spaces -= 1
    hashes += 2
    height -= 1
for i in range(stumpSpace):
    print(" ", end="")
print("#")

