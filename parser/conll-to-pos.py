#!/usr/bin/python


import sys

file = sys.argv[1]

separator = '_'

with open(file) as f:
    for line in f:
        tokens = line.split()
        if len(tokens) == 0:
            print ""
        else:
            word = tokens[1]
            tag = tokens[3]
            print "%s%s%s"%(word, separator, tag),
            
