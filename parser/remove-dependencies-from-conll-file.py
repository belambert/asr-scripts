#!/usr/bin/python

import sys

file = sys.argv[1]

for line in open(file):
    tokens = line.split()
    tokens = tokens[0:6]
    print "\t".join(tokens)
