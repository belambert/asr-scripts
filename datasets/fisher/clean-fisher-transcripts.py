#!/usr/bin/python


import sys
import re

file = sys.argv[1]

remove_periods_p = True

for line in open(file):
    line = line[:-1]

    first_paren = line.rfind("(")
    trans = line[:first_paren]
    id = line[first_paren:]
    
    # Remove [LAUGHTER] etc. ++NOISE++, 
    trans = re.sub("\[.*?\]", "", trans)
    trans = re.sub("\+\+.*?\+\+", "", trans)

    # Remove underscores (and periods, if indicated)
    trans = trans.replace("_", " ")
    if remove_periods_p:
        trans = trans.replace(".", " ")

    # Collapse sequences of spaces
    trans = re.sub(' +',' ', trans)
    trans = trans.strip()

    # If there's anything still left, print it:
    if len(trans) > 0:
        line = trans + " " + id
        print line
    

