#!/usr/bin/python

import sys, re

file = open(sys.argv[1])

# Don't assume the trailing apostrophe has something to to with possession?
final_apostrophe_exceptions = ["doin'", "o'", "ol'", "dunkin'", "goin'", "givin'", "somethin'"]

# Do something with these??!!
# internal_apostrophe_words = ["ma'am", "y'all", "don'ts", "c'mon", ]

def string_equal (s1, s2):
    return s1.lower() == s2.lower()


mappings = {"cannot": "can not",
            #'gonna': 'gon na',
            'gonna': 'going to',
            #'gotta': 'got ta',
            'gotta': 'got to',
            #'wanna': 'wan na',
            'wanna': 'want to',
            #'y'all': 'y' all', #or, no change.
            #"y'all": 'you all',
            "rock'n'roll" : "rock 'n' roll",
            #'kinda': 'kind a',
            'kinda': 'kind of',
            'lotta': 'lot of',
            'sorta': 'sort of',
            'outta': 'out of',
            'gotcha' : 'got you',
            'coupla' : 'couple of',
            'oughta': 'ought to',
            
            'dunno': "don't know",


            "'bout": "about",
            "'til": "until",
            "doin'": "doing",
            "'specially" : "especially",
            "'course" : 'of course',
            "'scuse": 'excuse',
            "'nother": 'another',
            "'cept" : 'except',
            "'round": "around",
            "ol'": "old",
            "'n'": "and",
            "'kay" : "okay",
            "d'ya": 'do you',
            "d'you": 'do you',
            "we'r": 'we are',

            "yea": "yeah",
            "don't": "do n't",  # This one isn't working for some reason?!?

            "jeeze": "jeez",


            # British to American spellings?
            'realise' : 'realize',
            'humour' : 'humor',
            'learnt' : 'learned',
            'programme' : 'program',

            # Change some punctuation...
            '-cause': "'cause",
            '-em': "'em",

            # Some common abbreviations...?
            'mr': "mister",
            'mr.': "mister",
            
            }

# If a word ends with one of these, strip off the ending
# and turn it into a token of its own.
endings = ["'s", "'m", "'d", "n't", "'re", "'ve", "'ll"]
            

def process_token(token):
    token = token.lower()

    if token in mappings:
        token = mappings.get(token)

    for ending in endings:
        if token.endswith(ending):
            break_point = len(token) - len(ending)
            token = "%s %s"%(token[0:break_point], token[break_point:])

    if token.endswith("s'"):
        token = "%s '"%token[:-1]


    # Remove any double spaces... we may have introduced them.
    token = re.sub("  +", " ", token)
    token = token.strip()

    return token

for line in file:
    tokens = line.split()
    tokens = map(process_token, tokens)
    line = ' '.join(tokens)
    print line
