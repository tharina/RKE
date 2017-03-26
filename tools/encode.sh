#!/bin/bash

DIR=$(dirname $0)/scripts

$DIR/manchester-encode.py | $DIR/build_packet.py | $DIR/sample.py $1
