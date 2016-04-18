#!/usr/bin/python

import sys

vocab_file = open(sys.argv[1])
dict_file = open(sys.argv[2])

def remove_alt_pron_marker(str):
    if str[-1] == ')' and str[-3] == '(':
        str = str[:-3]
    return str

vocab = {}
dict = {}

for word in vocab_file:
    word = word[:-1]
    vocab[word] = True

for line in dict_file:
    line = line[:-1]
    tokens = line.split()
    word = tokens[0]
    word = remove_alt_pron_marker(word)
    dict[word] = True

print "Vocab size: %d"%len(vocab)
print "Dict size:  %d"%len(dict)


vocab_not_in_dict = []
dict_not_in_vocab = []

for word in vocab.keys():
    if not word in dict:
        vocab_not_in_dict.append(word)

for word in dict.keys():
    if not word in vocab:
        dict_not_in_vocab.append(word)

print "Vocab items not in dict: %d"%len(vocab_not_in_dict)
print "Dict items not in vocab: %d"%len(dict_not_in_vocab)

print "Vocab items not in dict (partial):"
vocab_not_in_dict = vocab_not_in_dict[0:100]
for word in vocab_not_in_dict:
    print "     %s"%word

print "Dict items not in vocab (partial):"
dict_not_in_vocab = dict_not_in_vocab[0:100]
for word in dict_not_in_vocab:
    print "     %s"%word
