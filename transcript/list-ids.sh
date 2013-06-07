#!/usr/bin/python

import sys
import string

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines:
    tokens = line.split()
    # The ID is in the last token
    id = tokens[-1]
    # The ID is surrounded by parens, so remove those first
    id = id[1:-1]
    print id
