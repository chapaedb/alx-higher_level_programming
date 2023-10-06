#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

num = len(sys.argv)-1
if num == 0:
    print("0 arguments")
elif num == 1:
    print("1 argument ")
    print("{} : {}".format(num, sys.argv[num]))
else:
    print("{}: arguments".format(num))
    for key in range(num+1):
        print("{}: {}".format(key, sys.argv[key]))

