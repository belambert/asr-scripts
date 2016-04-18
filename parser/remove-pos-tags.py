#!/usr/bin/python

import sys,os
import string

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

lines = open(sys.argv[1]).readlines()

for line in lines:
    tokens = line.split()
    tokens = [token.split("_")[0] for token in tokens]
    print string.join(tokens, ' ')



