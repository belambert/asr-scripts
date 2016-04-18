#!/usr/bin/python

import sys
import collections

if len(sys.argv) != 2:
    print "Usage: %s <filename>"%sys.argv[0]

file=sys.argv[1]
code_table = collections.defaultdict(int)

for line in open(file):
    line = line[:-1]
    pivot=line.rfind("(")
    trans = line[:pivot]
    id = line[pivot+1:-1]

    # The speech type code
    code = id[3]

    # c (Common read no verbal punctuation) |
    # s (Spontaneous no/unspecified verbal punctuation) |
    # a (Adaptation read) |
    # r (Read version of spontaneous no verbal puncutation) |
    # o (cOmmon read with verbal puncuation) |
    # p (sPontaneous with verbal punctuation) |
    # e (rEad version of spontaneous with verbal punctuation )

    if code == 'c' or code == 's' or code == 'a' or code == 'r':
        print line

    code_table[code] += 1

for key in ['c', 's', 'a', 'r', 'o', 'p', 'e', 'z', 'X']:
    sys.stderr.write("%s   %d\n"%(key, code_table[key]))

