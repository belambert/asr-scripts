#!/usr/bin/python

import sys
import gzip
import os

if len(sys.argv) != 2:
    print "Usage: %s <pos tagged file>"%os.path.basename(sys.argv[0])
    exit(1)

file = sys.argv[1]

word_pos_delimiter = '_'

# Read in the Stanford POS file
if file.endswith(".gz"):
    f = gzip.open(file, 'rb')
    file_content = f.read()
    f.close()
    file_content = file_content.split('\n')
else:
    f = open(file)
    file_content = f.readlines()
    f.close()

# Then iterate through the lines, printing in CONLL
# format as we go
for line in file_content:
    tokens = line.split()
    index = 1
    for token in tokens:
        word, tag = token.split(word_pos_delimiter)
        #word, tag = token.split('_')
        print "%d\t%s\t%s\t%s\t%s\t%s"%(index, word, '_', tag, tag, '_')
        index += 1
    print ""
