#!/usr/bin/env python3
#
# Converts a lock signal into an unlock signal

import sys
from binascii import hexlify, unhexlify
from functools import reduce
from operator import xor

data = bytearray(unhexlify(sys.stdin.read().strip()))

data[1] = 2
data[9] = reduce(xor, data[1:9])

print(hexlify(data).decode('ascii'))
