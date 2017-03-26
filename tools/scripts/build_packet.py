#!/usr/bin/env python3
#
# Converts the payload into a full packet structure as expected by the car.

import sys

bits = sys.stdin.readline().strip()

preamble = '01' * 97

print(preamble + (bits + '01111111111') * 4 + '111')
