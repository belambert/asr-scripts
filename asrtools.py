#!/usr/bin/python

import sys
import os
import gzip
import exceptions
import editdistance

# Nbest stuff

class NBest:
    def __init__(self, sentences=None, header={}):
        for key, value in header.items():
            setattr(self, key, value)
        self.sentences = sentences
        for s in self.sentences:
            s.id = self.id
    
class Sentence:
    def __init__(self, words=None, total=None, acoustic=None, lm=None, id=None):
        self.words = words
        self.total = total
        self.acoustic = acoustic
        self.lm = lm
        self.id = id

    def wer(self):
        ref = reference_transcripts.get(self.id)
        sm = editdistance.SequenceMatcher(ref.words, self.words)
        return float(sm.distance()) / len(ref.words)

def string_to_float(s):
    "Given a string representing an int or float, convert it to such."
    try:
        return int(s)
    except exceptions.ValueError:
        return float(s)
        
def read_header(header_lines):
    "Given the header lines of an nbest list, convert them into a dict."
    header = {}
    for line in header_lines:
        tokens = line.split()
        tokens = tokens[1:]   # Get rid of the first token... it's '#'
        if len(tokens) == 1:
            header['id'] = tokens[0]
        else:
            header[tokens[0]] = string_to_float(tokens[1])
    return header
        
def read_nbest (filename):
    "Read in the n-best lines... that is everything that doesn't start with '#' or with 'End'"
    if filename.endswith('.gz'):
        lines = gzip.open(filename).readlines()
    else:
        lines = open(filename).readlines()
    sentence_lines = filter(lambda x: not x.startswith("#") and not x.startswith("End"), lines)
    header = read_header(filter(lambda x: x.startswith("#"), lines))
    sentences = map (nbest_line_to_sentence, sentence_lines)
    return NBest(sentences, header)

def nbest_line_to_sentence(line):
    "Convert a line of tokens into the words... that is every 4th word starting with the 9th..."
    tokens = line.split()
    total, acoustic, lm = int(tokens[1]), int(tokens[3]), int(tokens[5])
    tokens = tokens[9:]
    words = []
    for i in range(len(tokens)):
        if i%4 == 0:
            words.append(tokens[i].lower())
    words = clean_words(words)
    return Sentence(words, total, acoustic, lm)

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

# Reference transcripts....

def read_transcript(filename):
    sentences = []
    with open(filename) as f:
        for line in f:
            words, id = line.rsplit('(', 1)
            id = id.replace(')', '')
            s = Sentence(words.split(), id=id.strip())
            sentences.append(s)
    return sentences

reference_transcripts = {}

def load_reference_transcript(filename):
    global reference_transcripts
    sentences = read_transcript(filename)
    for s in sentences:
        reference_transcripts[s.id] = s

def get_reference_transcript(id):
    return reference_transcripts.get(id)
        
# Displaying stuff....

def clear_screen():
    "Write the ANSI code to clear the screen to stdout."
    print chr(27) + "[2J"

def display_nbest(nbest, max_count=10):
    clear_screen()
    print "ID: %s"%nbest.id
    print "ref: %s"%' '.join(reference_transcripts.get(nbest.id).words)
    for i in xrange(max_count):
        s = nbest.sentences[i]
        print "    %d. %s (%f)"%(i+1, ' '.join(s.words), s.wer())

load_reference_transcript("/Users/bel/sphinx/fisher/fisher-3-20.trans")
nbest = read_nbest("/Users/bel/005@fe_03_00550.ch2_38363-38522.nbest.gz")
