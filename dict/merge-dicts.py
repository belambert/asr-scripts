#!python

import sys
import re
from collections import defaultdict

dict_files = sys.argv[1:]

def remove_alt_pron(string):
    return re.sub('\(\d+\)$', '', string)

dictionary = defaultdict(list)

# First, read in all the dicts
for dict_file in  dict_files:
    sys.stderr.write("Reading dictionary: %s\n"%dict_file)
    with open(dict_file) as f:
        for line in f:
            tokens = line.split()
            if len(tokens) > 0:
                word = remove_alt_pron(tokens[0])
                word = word.lower()
                pron = tokens[1:]
                if pron not in dictionary[word]:
                    dictionary[word].append(pron)


for word in sorted(dictionary.keys()):
    prons = dictionary[word]
    for i in range(len(prons)):
        pron = prons[i]
        pron = ' '.join(pron)

        if i == 0:
            print "%s\t%s"%(word, pron)
        else:
            print "%s(%d)\t%s"%(word, i, pron)
