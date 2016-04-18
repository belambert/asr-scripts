#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print "Usage: %s <dict file>"%sys.argv[0]
    exit(-1)

dict_file = sys.argv[1]
phone_table = {}

for line in open(dict_file):
    tokens = line.split()
    if len(tokens) > 0:
        pron = tokens[1:]
        for phone in pron:
            phone_table[phone] = True

phones = phone_table.keys()
phones.sort()

for phone in phones:
    print phone

