#!/usr/bin/python3
"""Script to get stats from a request"""

import sys


STATUS = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
n = 0
try:
    for parameter in sys.stdin:
        line = parameter.split(" ")
        if len(line) > 2:
            status = line[-2]
            file_size = int(line[-1])
            if status in STATUS:
                STATUS[status] += 1
            total_size += file_size
            n += 1
            if n == 10:
                print("File size: {:d}".format(total_size))
                for key, value in sorted(STATUS.items()):
                    if value != 0:
                        print("{}: {:d}".format(key, value))
                n = 0
except KeyboardInterrupt:
    pass
finally:
    print("File size: {:d}".format(total_size))
    for key, value in sorted(STATUS.items()):
        if value != 0:
            print("{}: {:d}".format(key, value))
