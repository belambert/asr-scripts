#!/usr/bin/python

import sys
import re

if len(sys.argv) != 3:
    print "Usage: %s <vocab> <master dict>"%sys.argv[0]
    exit(-1)

vocab_file = open(sys.argv[1])
dict_file = open(sys.argv[2])

def remove_alt_pron_marker(str):
    if str[-1] == ')' and str[-3] == '(':
        str = str[:-3]
    return str

def remove_phoneme_numbers(str):
    word, part, phones = str.partition(' ')
    phones = re.sub("\d", "", phones)
    return "%s %s"%(word, phones)

vocab = []

for word in vocab_file:
    word = word[:-1]
    vocab.append(word)

dict = {}

master_dict_size = 0
new_dict_size = 0
for line in dict_file:
    line = line[:-1]
    if not line.startswith(';;;'):
        tokens = line.split()
        word = tokens[0]
        word = remove_alt_pron_marker(word)
        dict[word] = True

for word in vocab:
    if dict.get(word):
        print word
