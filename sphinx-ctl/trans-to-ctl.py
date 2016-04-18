#!/usr/bin/python

import sys

trans_file = sys.argv[1]

with open(trans_file) as f:
    for line in f:
        tokens = line.split()
        id = tokens[-1]
        id = id[1:-1]
        folder, rest = id.split('@')
        filename, times = rest.rsplit('_', 1)
        begin, end = times.split('-',1)
        print "%s/%s %s %s %s"%(folder, filename, begin, end, id)
