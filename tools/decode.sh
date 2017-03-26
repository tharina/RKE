#!/bin/bash

DIR=$(dirname $0)/scripts

$DIR/clockrec.py $1 2> /dev/null | $DIR/manchester-decode.rb | $DIR/bits2pdu.rb | $DIR/verify.py
