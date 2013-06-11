#!/usr/bin/python

import sys
import os

file = sys.argv[1]

class nbest:

    def __init__(self, sentences=None):
        self._sentences = sentences
    

def read_nbest_lines (filename):
    "Read in the n-best lines... that is everything that doesn't start with '#' or with 'End'"
    lines = open(filename).readlines()
    lines = filter(lambda x: not x.startswith("#") and not x.startswith("End"), lines)
    lines = map (lambda x: x.split(), lines)
    return lines

def nbest_line_to_words(line):
    "Convert a line of tokens into the words... that is every 4th word starting with the 9th..."
    line = line[9:]
    words = []
    for i in range(len(line)):
        if i%4 == 0:
            words.append(line[i])
    return words

def noise_word_p(word):
    "Check if a word begins and ends with ++"
    return word[0] == '+' and word[1] == '+' and word[-2] == '+' and word[-1] == '+'

def remove_alt_pron(word):
    "Remove the last three characters of a word if they look like (x)."
    if word[-1] == ')' and word[-3] == '(':
        word = word[:-3]
    return word

def clean_words(words):
    "Given some word, remove the noise words, silences, and alt pronunciations."
    words = filter(lambda x: not x == "<s>" and not x == "</s>" and not x == "<sil>" and not noise_word_p(x), words)
    words = map(remove_alt_pron, words)
    return words

def read_nbest(filename):
    

# nbest = read_nbest(file)
# for line in nbest:
#     words = nbest_line_to_words(line)
#     words = clean_words(words)
#     if len(words) == 0:
#         words = ["xxxxxxxxxx"]
#     new_line = ' '.join(words)
#     new_line = new_line.lower()
#     print new_line

    

