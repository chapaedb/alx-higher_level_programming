#!/usr/bin/env python3

for j in range(10):
    for k in range(j + 1, 10):
        print("{:d}{:d}".format(j, k), end="")
        if j != 8 or k != 9:
            print(", ", end="")
        else:
            print()
