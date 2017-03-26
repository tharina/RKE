#!/usr/bin/env python3
#
# Verifies the checksum of the packet

import sys
from binascii import hexlify, unhexlify
from functools import reduce
from operator import xor

data = bytearray(unhexlify(sys.stdin.read().strip()))

chksum = reduce(xor, data[1:9])
if chksum != data[9]:
    print("Error: invalid checksum!")
    sys.exit(-1)

print(hexlify(data).decode('ascii'))

