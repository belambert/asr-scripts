#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print "Usage: %s <dict file>"%sys.argv[0]
    exit(-1)

dict_file = sys.argv[1]
word_pron_separator = "\t"

def remove_alt_pron(str):
    if str[-1] == ')' and str[-3] == '(':
        str = str[:-3]
    return str

def get_alt_pron(str):
    if str[-1] == ')' and str[-3] == '(':
        return int(str[-2])
    return 0

def dict_compare(x, y):
    if remove_alt_pron(x) != remove_alt_pron(y):
        return x < y
    else:
        x0 = get_alt_pron(x)
        y0 = get_alt_pron(y)        
        return x0 < y0

dict_list = []
dict_table = {}

for line in open(dict_file):
    tokens = line.split()
    if len(tokens) > 0:
        word = tokens[0]
        pron = tokens[1:]
        pron = " ".join(pron)
        normalized_line = "%s%s%s"%(word, word_pron_separator, pron)

        if dict_table.get(word):
            print "ERROR: %s already encountered in dict file"%word
        else:
            dict_table[word] = True
        dict_list.append([word, normalized_line])

dict_list.sort(key=lambda x: x[0], cmp=dict_compare)

for entry in dict_list:
    word = entry[0]
    line = entry[1]

    # Make sure we have a pronunciation #0 of it...
    bare_word = remove_alt_pron(word)
    assert dict_table.get(bare_word)
    
    print line



    
