#/bin/sh
if [ $# \< 2 ]
then
    python3 ~/.bluetooth-proximity-locking/btpl.py [bluetooth address] > /dev/null &
elif [ "$1" = "-r" ] || [ "$1" = "--run" ]
    python3 ~/.bluetooth-proximity-locking/btpl.py [bluetooth address] > /dev/null &
elif [ "$1" = "-s" ] || [ "$1" = "--stop" ]
    pkill ~/.bluetooth-proximity-locking/btpl.py
fi
