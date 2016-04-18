#!/usr/bin/python

import sys
import string
import os

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%os.path.basename(sys.argv[0])
    exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines:
    # Split it into tokens
    tokens = line.split()
    # Remove the last one
    tokens = tokens[:-1]
    # Put it back together as a string
    s = string.join(tokens, ' ')
    # *Don't get rid of periods!*
    # s = s.replace('.','')

    # *BUT, LET'S REPLACE UNDER-SCORES WITH SPACES
    s = s.replace('_',' ')
    
    # Add a trailing period for the POS tagger

    # Only if it doesn't already end with a period?
    #if len(s) > 0 and not s[-1] == ".":
    #    s = s + " ."

    # No... we really want to make sure it doesn't merge sentences
    s = s + " ."            
    print s
