#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print "Usage: %s <id file> <ctl file>"%sys.argv[0]
    exit(-1)

id_file = sys.argv[1]
ctl_file = sys.argv[2]

ids = open(id_file).readlines()
ids = map(lambda x: x[:-1], ids)
id_table = {}
id_used_table = {}

for id in ids:
    id_table[id] = True

for line in open(ctl_file):
    line = line[:-1]
    tokens = line.split()
    id = tokens[-1]
    if id_table.get(id):
        print line
        id_used_table[id] = True
        #else:
        #sys.stderr.write("CTL ID '%s\' not in ID file.\n"%id)
        
    
# words_not_found = []
# for word in vocab_table.keys():
#     if vocab_used_table.get(word):
#         pass
#     else:
#         words_not_found.append(word)
# words_not_found.sort()
# for word in words_not_found:
#     sys.stderr.write("Vocab word '%s\' not in dictionary.\n"%word)
# sys.stderr.write("%d words not found"%len(words_not_found))




