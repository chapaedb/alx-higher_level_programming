#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    num = len(sys.argv)-1
    print("Number of argument(s):", num, end="")
    if num == 0:
        print(".", end="\n\n")

    else:
        print(":", end="\n\n")
        for key in range(1,num+1):
            print("{}: {}".format(key, sys.argv[key]))
`
