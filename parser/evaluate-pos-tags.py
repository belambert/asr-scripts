#!/usr/bin/python

## TODO: Print confusion matrix...?
## Does NLTK have code for evaluating POS tags?

import sys
import re
import os
from collections import defaultdict

if len(sys.argv) != 3 and len(sys.argv) != 4:
    print "Usage: %s <ref file> <hyp file> [verbose]"%os.path.basename(sys.argv[0])
    exit(1)


if len(sys.argv) == 4:
    verbose=True
else:
    verbose=False

ref_tag_file = sys.argv[1]
hyp_tag_file = sys.argv[2]

def format_pair(pair):
    return "%4s %4d"%(pair[0], pair[1])

def format_pair_dense(pair):
    return "%s %d"%(pair[0], pair[1])

def list_to_count_list(list):
    table = defaultdict(int)
    for e in list:
        table[e] += 1
    return sorted(table.items(), key=lambda x: x[1], reverse=True)

def evaluate_pos_tags (reference, hypothesis, verbose=False):
    "Perform an evaluation of automatic POS-tagging.  SWB expts have shown the to be aroun 95%-96%, with fine-grained classes."
    reference_tokens = []
    hypothesis_tokens = []
    token_count = 0
    correct_count = 0
    pos_count = defaultdict(int)
    pos_correct_count = defaultdict(int)
    mistakes = defaultdict(list)

    # Read in the reference and hypothesis files
    with open(reference) as f:
        ref_lines = f.readlines()
    with open(hypothesis) as f:
        hyp_lines = f.readlines()

    # Split into tokens and put sentences onto lists, checking that the # of words match as we go...
    for ref, hyp in zip(ref_lines, hyp_lines):
        ref_tokens = ref.split()
        hyp_tokens = hyp.split()
        if len(ref_tokens) != len(hyp_tokens):
            print "ERROR: TOKEN LENGTHS DON'T MATCH!!"
            print "REF: %s"%ref_tokens
            print "HYP: %s"%hyp_tokens
            exit()
        reference_tokens.extend(ref_tokens)
        hypothesis_tokens.extend(hyp_tokens)

    print "%s reference tokens; %s hypothesis tokens."%(len(reference_tokens), len(hypothesis_tokens))
    assert (len(reference_tokens) == len(hypothesis_tokens))
    
    reference_tokens = map(lambda x: x.split('_'), reference_tokens)
    hypothesis_tokens = map(lambda x: x.split('_'), hypothesis_tokens)

    for r, h in zip(reference_tokens, hypothesis_tokens):
        ref_tag = r[1]
        hyp_tag = h[1]
        if ref_tag != ".":
            token_count += 1
            pos_count[ref_tag] += 1
            assert (r[0] == h[0])

            if ref_tag == hyp_tag:
                correct_count += 1
                pos_correct_count[ref_tag] += 1
            else:
                # Save what the mistake was
                mistakes[ref_tag].append(hyp_tag)

    print "%d / %d correct [%f %%]"%(correct_count, token_count, ((1.0 * correct_count / token_count) * 100))

    if verbose:
        # Compute accuracies for each POS tag
        accuracies = []
        for key in pos_count.keys():
            count_correct = pos_correct_count[key]
            count = pos_count[key]
            accuracy = (1.0 * count_correct / count) if count_correct else 0.0
            accuracies.append([key, accuracy])
    # Sort the tags by their accuracies
        accuracies = sorted(accuracies, key=lambda x: x[1], reverse=True)
        for pos, acc in accuracies:
            this_mistakes = mistakes[pos]
            this_mistakes = list_to_count_list(this_mistakes)
            this_mistakes = map(format_pair_dense, this_mistakes)
            print "%10s   %5.3f   (%6d / %6d)  [%s]"%(pos, acc, pos_correct_count[pos], pos_count[pos],
                                                      ', '.join(map(str, this_mistakes)) )

print "Evaluation code loaded... now evaluating using ref %s and hypothesis %s."%(ref_tag_file, hyp_tag_file)
evaluate_pos_tags(ref_tag_file, hyp_tag_file, verbose=verbose)




	 




	  


    


