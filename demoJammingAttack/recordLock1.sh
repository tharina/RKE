..grc/record_jamming.py --outfile lock1.record
..grc/demod.py --infile lock1.record --outfile lock1.bytes
../tools/decode.sh lock1.bytes
