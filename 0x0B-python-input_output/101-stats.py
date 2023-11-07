#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Accumulated file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(accumulated_size, accumulated_status_codes):
    """Print accumulated metrics.

    Args:
        accumulated_size (int): The accumulated file size.
        accumulated_status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(accumulated_size))
    for code in sorted(accumulated_status_codes):
        print("{}: {}".format(code, accumulated_status_codes[code]))


if __name__ == "__main__":
    import sys

    accumulated_size = 0
    accumulated_status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(accumulated_size, accumulated_status_codes)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                size = int(line[-1])
                accumulated_size += size
            except (IndexError, ValueError):
                pass

            try:
                status_code = line[-2]
                if status_code in valid_codes:
                    if status_code not in accumulated_status_codes:
                        accumulated_status_codes[status_code] = 1
                    else:
                        accumulated_status_codes[status_code] += 1
            except IndexError:
                pass

        print_stats(accumulated_size, accumulated_status_codes)

    except KeyboardInterrupt:
        print_stats(accumulated_size, accumulated_status_codes)
        raise
