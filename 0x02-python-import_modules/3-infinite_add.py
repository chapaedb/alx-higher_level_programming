#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    count = len(sys.argv) - 1
    added = 0

    for x in range(1, count + 1):
        added += int(sys.argv[x])

    print(added)
