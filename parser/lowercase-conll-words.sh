#!/usr/bin/python

import sys
import gzip
import os

if len(sys.argv) != 2:
    print "Usage: %s <CONLL file>"%os.path.basename(sys.argv[0])
    exit(1)

file = sys.argv[1]

for line in open(file):
    tokens = line.split()
    if len(tokens) > 1:
        tokens[1] = tokens[1].lower()
        print '\t'.join(tokens)
    else:
        print ""

