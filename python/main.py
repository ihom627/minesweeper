#!/usr/bin/env python
# Copyright (c) 2015, RetailNext, Inc.
# This material contains trade secrets and confidential information of
# RetailNext, Inc.  Any use, reproduction, disclosure or dissemination
# is strictly prohibited without the explicit written permission
# of RetailNext, Inc.
# All rights reserved.

import sys
from game import Game

def main():
    if len(sys.argv) != 4:
        print "usage: %s <width> <height> <mines>" % sys.argv[0]
        exit(1)
    g = Game(*map(lambda x: int(x), sys.argv[1:]))
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        line = line.rstrip()
        cmd, x, y = line.split()
        x = int(x)
        y = int(y)
        if cmd == "reveal":
            count = g.reveal(x,y)
            print count
        else:
            sys.stderr.write('unknown command: %s\n' % line)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
