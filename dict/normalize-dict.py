#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print "Usage: %s <dict file>"%sys.argv[0]
    exit(-1)

dict_file = sys.argv[1]
word_pron_separator = "\t"

for line in open(dict_file):
    tokens = line.split()
    if len(tokens) > 0:
        word = tokens[0]
        pron = tokens[1:]
        pron = " ".join(pron)
        print "%s%s%s"%(word, word_pron_separator, pron)


    
    
