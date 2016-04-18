#!/usr/bin/python

import sys
import string
import blambert_util as bl

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines:
    tokens = line.split()
    tokens = filter(lambda x: not x.startswith("++") and not x.endswith("++") , tokens)
    print string.join(tokens, ' ')



