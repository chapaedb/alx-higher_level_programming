#!/usr/bin/python3

def fizzbuzz():
    """ Prints fizz for multiple of 3
    buzz for 5 and fizzbuzz for multiple of both"""
    for i in range(100):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
