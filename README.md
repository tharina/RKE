# Remote Keyless Entry Systems

Collection of scripts and GnuRadio graphs for researching Remote Keyless Entry systems for automobiles.

## Contents

#### tools/

tools/decode.sh
    Takes the output of the demod.grc graph (i.e. a bytestream consisting of zeroes and ones) and decodes it to the underlying packet.
    Does the following internally:
    - Clock recovery
    - Manchester decoding
    - PDU reassembling

tools/encode.sh
    Takes a packet represented as hexadecimal and produces a bytestream that can be fed to mod.grc for sending.
    Does the following internally:
    - Manchester encoding
    - Packet assembly
    - "Sampling" at 2MHz

tools/scripts:
    Various small scripts that are used by decode.sh and encode.sh. See the comments in each file for more information.

#### grc/

GNURadio flow graphs.

#### diagrams/

Jupyter scripts that were used to generate the modulation images for the slides.

#### demoJammingAttack/

The jamming attack presented in the last slides.

    1. Start the jammer
    2. ./recordLock1.sh
        owner send lock signal, car doesn't lock due to jammer
    3. ./recordLock2.sh
        owner sends another lock signal, car still doesn't lock
    4. ./sendLock1.sh
        stops the jammer, send first signal
        car is now locked, owner walks away
    5. ./sendUnlock2.sh
        converts second signal to unlock signal
        car is unlocked by attackers
