#!/usr/bin/env python3

for j in range(10):
    for k in range(j + 1, 10):
        if j == 8 and k == 9:
            print("{}{}".format(j, k))
        else:
            print("{:d}{:d}".format(j, k), end=",")

