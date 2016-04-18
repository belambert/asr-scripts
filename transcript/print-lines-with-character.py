#!/usr/bin/python

import sys
import re

file = sys.argv[1]

#char = "_"
#char = "."
char = "'"

for line in open(file):

    line = line[:-1]    

    first_paren = line.rfind("(")
    trans = line[:first_paren]
    id = line[first_paren:]

    #if char in trans:
    #    print trans

    tokens = trans.split()
    
    #if any(map(lambda x: x.endswith("-"), tokens)):
    if any(map(lambda x: x.startswith("-"), tokens)):
        print line

