#!/usr/bin/env pypy3
#
# Detects a signal in a bytestream produced from demod.grc and performs clock recovery. Then outputs the resulting bitstream.

import sys

with open(sys.argv[1], 'rb') as f:
    data = f.read()

msg = []

samples_per_symbol = 900

# Current position in the buffer
current_position = 0
# Right after the first candidate
checkpoint = -1


def find_start():
    global current_position, checkpoint, data

    # Look for > samples_per_symbol ones
    one_found = False
    count = 0

    while current_position < len(data):
        b = data[current_position]
        if not one_found and b == 1:
            one_found = True
            count = 0
        elif one_found and b == 0:
            if count < samples_per_symbol or count > 2 * samples_per_symbol:
                # False candidate
                one_found = False
            else:
                # Looks good
                checkpoint = current_position
                return

        count += 1
        current_position += 1

    print("Error: start not found", file=sys.stderr)
    sys.exit(-1)


while current_position < len(data):

    find_start()
    msg = [0, 1]

    current_symbol = 0
    current_length = 0
    need_verify = True

    # Try to receive the whole packet now
    while current_position < len(data):

        b = data[current_position]

        if current_symbol != b:
            # Verify last 10 symbols were same as this one
            invalid = False
            for i in range(10):
                if data[current_position-i] != b:
                    invalid = True

            if not invalid:
                mult = int(current_length / (samples_per_symbol * 1))
                if mult > 2 and current_symbol == 0 and len(msg) > 50:
                    print("done", file=sys.stderr)
                    break

                #for i in range(mult):
                    #print(current_symbol, current_length // mult, file=sys.stderr)
                msg += [current_symbol] * mult

                current_length = 10
                current_symbol = b


        if need_verify and len(msg) > 25:
            fail = False
            for i, b in enumerate(msg):
                if msg[i] != i % 2:
                    fail = True
                    break

            if fail:
                print("Got incorrect signal, restarting from last checkpoint", file=sys.stderr)
                current_position = checkpoint
                break
            else:
                need_verify = False

        current_length += 1
        current_position += 1

print(''.join(map(str, msg)))
