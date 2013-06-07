#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print "Usage: %s <mdef file>"%sys.argv[0]
    exit(-1)


mdef_file = sys.argv[1]
phone_table = {}
def_section_p = False
for line in open(mdef_file):
    if def_section_p:
        tokens = line.split()
        if len(tokens) > 0:
            phone = tokens[0]
            if phone[0] != '+':
                phone_table[phone] = True
    if line.startswith("#base "):
        def_section_p = True

phones = phone_table.keys()
phones.sort()

for phone in phones:
    print phone
