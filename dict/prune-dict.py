#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print "Usage: %s <vocab file> <dict file>"%sys.argv[0]
    exit(-1)

vocab_file = sys.argv[1]
dict_file = sys.argv[2]

vocab = open(vocab_file).readlines()
vocab = map(lambda x: x[:-1], vocab)

vocab_table = {}
vocab_used_table = {}

for word in vocab:
    vocab_table[word] = True


def remove_alt_pron(str):
    if str[-1] == ')' and str[-3] == '(':
        str = str[:-3]
    return str

for line in open(dict_file):
    line = line[:-1]
    tokens = line.split()
    word = tokens[0]
    true_word = remove_alt_pron(word)

    if vocab_table.get(true_word):
        print line
        vocab_used_table[true_word] = True
        #else:
        #sys.stderr.write("Vocab word '%s\' not in dictionary.\n"%word)
    

words_not_found = []

for word in vocab_table.keys():
    if vocab_used_table.get(word):
        pass
    else:
        words_not_found.append(word)

words_not_found.sort()

for word in words_not_found:
    sys.stderr.write("Vocab word '%s\' not in dictionary.\n"%word)


sys.stderr.write("%d words not found"%len(words_not_found))




