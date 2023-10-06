#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    num = len(sys.argv) - 1
    if num == 0:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{}: argument".format(num))
        print("{}: {}".format(num, sys.argv[num]))
    else:
        print("{} arguments:".format(num))
        for i in range(1, num + 1):
            print("{}: {}".format(i, sys.argv[i]))
