#!/usr/bin/python

import sys
import string
import collections

file = sys.argv[1]

def punc_token_p(str):
    return str[0] in string.punctuation

punc_table = collections.defaultdict(int)

for line in open(file):
    line = line[:-1]
    tokens = line.split()
    tokens = tokens[:-1]    
    for token in tokens:
        if punc_token_p(token):
            punc_table[token] += 1

for punc in punc_table.keys():
    print "%s   %d"%(punc, punc_table[punc])
