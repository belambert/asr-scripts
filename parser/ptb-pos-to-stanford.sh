#!/usr/bin/python

## Copyright Benjamin E. Lambert, 2005-2011
## All rights reserved
## Please contact author regarding licensing and use:
## ben@benjaminlambert.com

import sys
import re
import os
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

if len(sys.argv) != 2:
    print "Usage: %s <ptb file>"%os.path.basename(sys.argv[0])
    exit(1)

infile = sys.argv[1]
#outfile = sys.argv[2]
#outfile = infile+".stnfd"
outfile = infile

write_sentence_period = False

# For the output...
separator = '_'


# Words are separated from their part-of-speech tag by a forward slash.  In
# cases of uncertainty concerning the proper part-of-speech tag, words are
# given alternate tags, which are separated from one another by a vertical
# bar.  The order in which the alternate tags appear is not significant, but
# has not been standardized. In the Switchboard data, there are also tags
# including carets (^), which indicate various kinds of transcription errors.

buggy_tokens = 0
token_count = 0

def decimal_string (num):
    "Return the given number as a string, including commas between 100's, 1k's, 1m's, etc."
    return locale.format("%d", num, grouping=True)

def fix_token (token):
    global buggy_tokens
    if len(token) != 2:
        print token
    if "|" in token[1]:
        # The pipe symbol means they weren't sure, so just use the first.
        token[1] = token[1].split('|')[0]
        buggy_tokens += 1
    if "^" in token[1]:
        # The caret means that there was an error in the transcription,
        # Ideally we'd fix these, but let's just choose the first...
        # It's better than discarding the word because we don't want to break
        # the flow of words
        token[1] = filter(lambda x: x != '',  token[1].split('^'))[0]
        buggy_tokens += 1
    return token


def read_swb_file (filename):
    global token_count
    # Read the SWB file into a list of lines
    with open(filename) as f:
        lines = f.readlines()
    lines = map(lambda x: x.rstrip('\n'), lines)
    
    token_buffer = []
    sentences = []

    for line in lines:
        if not ("*x*" in line or "===" in line or line == ""):
            line = "  %s  "%line
                        
            # Get rid of the "speaker" markings
            if re.search("Speaker\w*/SYM", line):
                line = re.sub("Speaker\w*/SYM", "", line)
            if re.search("\S+/:", line):
                line = re.sub("\S+/:", " ", line)

            # Remove everything that can be string substituted, and replaced by a space... mostly brackets and punctuation.
            remove_list =["[", "]", "./.", ",/,", "?/.", "!/.", "``/``", "''/''", "'/POS", "--/:"]
            for remove in remove_list:
                if remove in line:
                    line = line.replace(remove, " ")

            # Get rid of everything where the "word" is just some punctuation... these are artifacts of the manual annotation (probably)
            prefix_char_class = "[,.'!]"
            if re.search("\s%s+/\S+"%prefix_char_class, line):
                line = re.sub("\s%s+/\S+"%prefix_char_class, " ", line)

            # Now destroy some remaining punctuation, by substituting with nothing.
            #delete_list = ["-", "'", "(", ")"]
            delete_list = ["(", ")"]
            for to_delete in delete_list:
                if to_delete in line:
                    line = line.replace(to_delete, "")

            # If the line doesn't consist entirely of spaces...(?)... then split it into tokens and save the tokens?
            if not re.match("^\s*$", line):
                line = line.upper()
                tokens = re.split("\s+", line)
                # For each token, split the word apart from the POS tag
                tokens = map(lambda x: x.split('/'), tokens)
                tokens = filter(lambda x: len(x) == 2, tokens)
                tokens = map(fix_token, tokens)
                for token in tokens:
                    token_count += 1
                    token_buffer.append(token)
                        
        # O/w we're between utterances, so write what we've got and clear the buffer
        else:
            #if token_buffer != [] and len(token_buffer) > 1:
            if token_buffer != []:
                sentences.append(token_buffer)
                token_buffer = []
    return sentences

def write_with_pos(sentences, filename):
    "Write the sentences with parts-of-speech."
    with open(filename, 'w') as out:
        for sentence in sentences:        
            for token in sentence:
                out.write("%s%s%s "%(token[0], separator, token[1]))
            if write_sentence_period:
                out.write("._.\n")
            else:
                out.write("\n")

def write_without_pos(sentences, filename):
    "Write the sentences without parts-of-speech."
    with open(filename, 'w') as out_no_pos:
        for sentence in sentences:
            for token in sentence:
                out_no_pos.write("%s "%token[0])
            if write_sentence_period:
                out_no_pos.write(".\n")
            else:
                out_no_pos.write("\n")


def write_stanford_file (sentences, filename):
    word_count = sum(map(len, sentences))
    sentence_count = len(sentences)
    print "Writing %s sentences, containing %s total words, %.4f avg words per sentence."%(decimal_string(sentence_count), decimal_string(word_count), float(word_count) / sentence_count)
    write_with_pos(sentences, outfile + ".txt")
    write_without_pos(sentences, outfile + "-no-pos.txt")

    # Split the sentences into halves and write them as train/test sets
    #cutoff = sentence_count / 2
    #train_sentences = sentences[:cutoff]
    #test_sentences = sentences[cutoff:]
    #write_with_pos(train_sentences, outfile + "-train.txt")
    #write_without_pos(train_sentences, outfile + "-train-no-pos.txt")
    #write_with_pos(test_sentences, outfile + "-test.txt")
    #write_without_pos(test_sentences, outfile + "-test-no-pos.txt")


def convert_swb_pos_tags (infile, outfile):
    "Convert a SWB POS-tagged training example file to a file format that can be used to train the Stanford POS tagger. (?)"
    sentences = read_swb_file(infile)
    write_stanford_file(sentences, outfile)
    

print "Conversion code loaded... now converting SWB file '%s' to Stanford file '%s'."%(infile, outfile)
convert_swb_pos_tags(infile, outfile)
print "Converted %s tokens.  %s (%.4f %%) tokens were buggy."%(decimal_string(token_count), decimal_string(buggy_tokens), 100 * float(buggy_tokens) / token_count)


