#!/usr/bin/python

import sys
import string
import re

if len(sys.argv) != 2:
    print "Usage: %s <transcript file>"%sys.argv[0]
    exit(-1)

f = open(sys.argv[1])
lines = f.readlines()

for line in lines:
    line = line[:-1]

    left_paren = line.rfind("(")
    right_paren = line.rfind(")")

    id = line[left_paren+1:right_paren]
    print id

	
