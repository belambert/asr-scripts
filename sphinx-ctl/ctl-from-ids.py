#!/usr/bin/python

import sys

file = sys.argv[1]

for line in open(file):    
    line = line.strip()
    last_paren = line.rfind("_")
    last_token = line[last_paren+1:]
    rest = line[:last_paren]
    last_paren = rest.rfind("_")
    penultimate_token = rest[last_paren+1:]
    filename = rest[:last_paren]
    print "%s %s %s %s"%(filename, penultimate_token, last_token, line)
