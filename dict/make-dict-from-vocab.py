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

vocab = {}
vocab_words_found = {}

for word in vocab_file:
    word = word[:-1]
    vocab[word] = True

master_dict_size = 0
new_dict_size = 0
for line in dict_file:
    line = line[:-1]
    if not line.startswith(';;;'):
        tokens = line.split()
        word = tokens[0]
        word = remove_alt_pron_marker(word)
        master_dict_size += 1
        if vocab.get(word):
            vocab_words_found[word] = True
            new_dict_size += 1
            print remove_phoneme_numbers(line)

sys.stderr.write('Master dict size:            %d\n'%master_dict_size)
sys.stderr.write('Vocab size:                  %d\n'%len(vocab))
sys.stderr.write('New dict size:               %d\n'%new_dict_size)

vocab_not_in_dict = []

for word in vocab.keys():
    if not vocab_words_found.get(word):
        vocab_not_in_dict.append(word)

sys.stderr.write('Vocab not present in dict:   %d\n'%len(vocab_not_in_dict))

for word in vocab_not_in_dict:
    sys.stderr.write('%s\n'%word)




