#!/usr/bin/python

import sys
import collections

if len(sys.argv) != 2:
    print "Usage: %s <filename>"%sys.argv[0]

file=sys.argv[1]

id_printed_table = {}
id_counted_table = {}
#trans_table = {}

code_table = collections.defaultdict(int)

for line in open(file):
    line = line[:-1]
    pivot=line.rfind("(")
    trans = line[:pivot]
    id = line[pivot+1:-1]

    id1, id2 = id.split()

    # The speech type code
    code = id1[3]

    # c (Common read no verbal punctuation) |
    # s (Spontaneous no/unspecified verbal punctuation) |
    # a (Adaptation read) |
    # r (Read version of spontaneous no verbal puncutation) |
    # o (cOmmon read with verbal puncuation) |
    # p (sPontaneous with verbal punctuation) |
    # e (rEad version of spontaneous with verbal punctuation )

    #if id2 not in id_table and (code == 'c' or code == 's' or code == 'a' or code == 'r' ):
    #if id2 not in id_table and (code == 'c' or code == 's' or code == 'r' ):


    #if id2 not in id_counted_table:
    if id2 not in id_printed_table:
        id_counted_table[id2] = True
        code_table[code] += 1

    #if id2 not in id_printed_table and (code == 'c' or code == 's' or code == 'r' ):
    if id2 not in id_printed_table and code == 'c' :
        id_printed_table[id2] = True
        print line


#for key in code_table.keys():
#for key in ['c', 's', 'a', 'r', 'o', 'p', 'e', 'z', 'X']:
#    sys.stderr.write("%s   %d\n"%(key, code_table[key]))

