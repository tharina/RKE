#!/usr/bin/env python3
#
# Applies manchester encoding to the given bitstream

import sys
import binascii

data = binascii.unhexlify(sys.stdin.read().strip())
output = []

for byte in data:
    bits = format(byte, '0>8b')

    for c in bits:
        if c == '0':
            output.append('01')
        elif c == '1':
            output.append('10')
        else:
            assert(False)

print(''.join(output))
