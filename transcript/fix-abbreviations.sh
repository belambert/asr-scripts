#!/usr/bin/python


import sys
import re
import string
import itertools

#sphinx_file=sys.argv[1]
sphinx_lines = []

def single_letter_p(str):
    return len(str) == 1

def get_candidate_abbreviations(tokens):
    begin = None
    end = None
    spans = []
    for i in range(len(tokens)):
        token = tokens[i]
        if single_letter_p(token):
            if begin != None:  # We're in the middle of an abbreviation... keep going til we see a full word
                pass
            else:      # We're at the beginning of a possible abbrevation
                begin = i
        else:
            if begin != None:
                end = i
                spans.append([begin, end])
                begin = None
                end = None
    return spans


def isolated_letter_p(tokens, i):
    if i>0 and len(tokens[i-1]) == 1:
        return False
    if i != len(tokens)-1 and len(tokens[i+1]) == 1:
        return False
    return True

# def punctuate_abbrevations(tokens):
#     new_tokens = list(tokens)
#     for i in range(len(tokens)):
#         word = tokens[i]
#         if len(word) == 1:
#             if word == "A" or word == "I":
#                 if isolated_letter_p(tokens, i):
#                     pass
#                 else:
#                     # Make sure we're not in a sequence of stuttering: "A A A AN ..." or "I I I I am..."
#                     # The extra check for an 'F' is to identify the last 'A' in "F A A" properly
#                     # F A A seems to be the only special case abbrevation we need to look for in this data set.
#                     # But there are potentually many, e.g. "A A" (Alcoholics Anonymous) or "I I S" (Microsoft's web server)
#                     if i > 1 and tokens[i-1] == word and (i==1 or tokens[i-2] != 'F'):
#                         pass
#                     else:
#                         new_tokens[i] = word + "."                    
#             else:
#                 new_tokens[i] = word + "."
#     return new_tokens

def punctuate_abbrevations(tokens):
    new_tokens = list(tokens)
    spans = get_candidate_abbreviations(tokens)
    for [begin, end] in spans:
        abbrev = tokens[begin:end]
        if all(map(lambda x: x == 'A', abbrev)) or all(map(lambda x: x == 'I', abbrev)):
            pass
        else:
            for i in range(begin, end):
                new_tokens[i] = tokens[i] + "."
            print new_tokens
    return new_tokens

def print_isolated_abbrevation(tokens):
    for i in range(len(tokens)):
        word = tokens[i]
        if len(word) == 1:
            if word == "A" or word == "I":
                if isolated_letter_p(tokens, i):
                    print ' '.join(tokens)
                    return


def repuncutate_file(file):
    for line in open(file).readlines():
        m = re.match("(.*)\((.+)\)", line)
        trans = m.group(1)
        id = m.group(2)
        tokens = trans.split()
        tokens = punctuate_abbrevations(tokens)
        trans = ' '.join(tokens)
        #print "%s (%s)"%(trans, id)

def print_isolated_abbrevations(file):
    for line in open(file).readlines():
        m = re.match("(.*)\((.+)\)", line)
        trans = m.group(1)
        id = m.group(2)
        tokens = trans.split()
        print_isolated_abbrevation(tokens)
    

#repuncutate_file(sphinx_file)
#print_isolated_abbrevations(sphinx_file)
