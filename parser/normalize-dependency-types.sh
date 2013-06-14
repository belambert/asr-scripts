#!/usr/bin/python

import sys

file=sys.argv[1]

with open(file) as f:
    for line in f:
        tokens = line.split()
        if len(tokens) >= 8:
            tokens[7] = tokens[7].lower()
        print '\t'.join(tokens)
