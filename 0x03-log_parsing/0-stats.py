#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line must be
skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for
this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not have
the same output as this one.
"""

import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_statistics():
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                sc = data[-2]
                if sc in stats:
                    stats[sc] += 1
            except (IndexError, KeyError):
                pass
            try:
                filesize += int(data[-1])
            except (TypeError, IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_statistics()
        print_statistics()
    except KeyboardInterrupt:
        print_statistics()
        raise
