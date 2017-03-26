for pid in $(pgrep python2); do
    if ps $pid | grep -q jamming.py; then
        echo "Stopping jammer (pid = $pid)"
        kill -s 2 $pid
    fi
done

../grc/mod.py --infile lock1.bytes
