#!/usr/bin/env python3
#
# "Samples" the packet at roughly 2MHz

import sys

one = 990 * b'\x01'
first_one = 905 * b'\x01'
zero = 1100 * b'\x00'

is_first_one = True

output = open(sys.argv[1], 'wb')

line = sys.stdin.readline().strip()
for c in line.strip():
    if c == '0':
        output.write(zero)
    elif c == '1':
        if is_first_one:
            output.write(first_one)
            is_first_one = False
        else:
            output.write(one)
    else:
        assert(False)

for _ in range(4):
    output.write(zero)

output.close()
