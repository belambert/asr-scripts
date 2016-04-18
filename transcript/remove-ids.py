#!/usr/bin/python

import sys
import re 

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%sys.argv[0]
    exit(-1)

file = sys.argv[1]

for line in open(file):
    line = line[:-1]

    first_paren = line.rfind("(")
    trans = line[:first_paren]
    id = line[first_paren:]
    
    trans = re.sub(' +',' ', trans)
    trans = trans.strip()

    print trans
