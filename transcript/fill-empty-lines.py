#!/usr/bin/python

import sys

file = open(sys.argv[1])
filler = sys.argv[2]


for line in file:
    line = line[:-1]
    
    if line == "":
        line = filler

    print line
    

