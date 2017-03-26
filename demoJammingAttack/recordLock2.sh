..grc/record_jamming.py --outfile lock2.record
..grc/demod.py --infile lock2.record --outfile lock2.bytes
../tools/decode2unlock.sh lock2.bytes
