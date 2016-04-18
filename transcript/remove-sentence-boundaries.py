#!/usr/bin/python

import sys
import string
import lisp

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

# Read in the file
with open(sys.argv[1]) as f:
    lines = f.readlines()

# Re-print without sentence boundaries
for line in lines:
    tokens = line.split()
    tokens = filter(lambda x: not lisp.string_equal(x,"<s>") and not lisp.string_equal(x,"</s>"), tokens)
    print string.join(tokens, ' ')



