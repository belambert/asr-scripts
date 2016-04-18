#!/opt/local/bin/python

import sys, re
import argparse

parser = argparse.ArgumentParser(description='Condition speech (auto) transcription to remove speech artifacts, including disfluencies.')
parser.add_argument("filename", help="Transcript filename.")
parser.add_argument('-nh', '--remove-hyphen-lines', action='store_true', help='print the individual sentences and their errors')
parser.add_argument('-hi', '--has-ids', action='store_true', help='hypothesis and reference files have ids in the last token?')
parser.add_argument('-i', '--include-sentence-ids', action='store_true', help='print tables of which words were confused')
parser.add_argument('-d', '--dummy-token', default=None, help='token to print when all tokens have been removed from a line')
parser.add_argument('-min', '--min-length', default=0, type=int, help='minimum transcript length to include (in token count)')
parser.add_argument('-max', '--max-length', default=sys.maxint, type=int, help='maximum transcrip length to include (in token count)')
args = parser.parse_args()

file = args.filename
include_sentence_id = args.include_sentence_ids
remove_hyphen_lines = args.remove_hyphen_lines
file_has_ids = args.has_ids
dummy_token = args.dummy_token
min = args.min_length
max = args.max_length

def remove_alt_pron_marker(str):
    if len(str)>3 and str[-1] == ')' and str[-3] == '(':
        str = str[:-3]
    return str

# Define the disfluencies we want to remove
dis = ('um',
       'uh',
       'mm',
       'ah',
       'er',
       'eh',
       'mhm',
       'hm',
       'ha',
       'huh',
       'uhuh',
       'uh-uh',
       'uh-huh',
       'huh-',
       'huh-huh',
       'uh-oh',
       'um-hum',
       'uh-hum',
       'ahah',
       'heh',
       'hmm',
       'aha',
       'aw',
       'mh-',
       # Do these count?
       #'ooh',
       #'oh',
       )
dis = map(str.lower, dis)
dis = dict((w,None) for w in dis)

with open(file) as f:
    for line in f:
        # Split into tokens throwing away that last one which is the ID        
        tokens = line.split()
        if file_has_ids:
            sid = tokens[-1]
            tokens = tokens[:-1]
        # Put the line back together without the ID so
        # we can check for hypthens and substitute
        # puncutation
        line = ' '.join(tokens)
        # If we're filtering hyphens and we find one, skip
        if remove_hyphen_lines and '-' in line:
            continue
        # Replace the puncutation with spaces
        line = re.sub('[?!,~;.]', ' ', line)
        # Remove hyphens!!!???
        #line = line.replace('-', ' ')
        tokens = line.split()
        tokens = filter(lambda x: x.lower() not in dis, tokens)
        # And get rid of noise markers
        tokens = filter(lambda x: '++' not in x, tokens)
        tokens = map(remove_alt_pron_marker, tokens)
        # Check that the length is OK
        if min and len(tokens) < min:
            continue
        elif max and len(tokens) > max:
            continue
        # Finally print the line
        if include_sentence_id:
            tokens.append(sid)
        if len(tokens) > 0:
            print ' '.join(tokens)
        else:
            if dummy_token:
                print dummy_token
