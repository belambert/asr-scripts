#!/usr/bin/python

import sys, re


# (defparameter *disfluency-list*
#   '(UM
#     UH
#     MM
#     AH
#     ER
#     EH
#     EH-
#     MHM
#     HM
#     HA
#     HUH
#     UH-HUH))

# Define the disfluencies we want to remove
# dis = ('um',
#        'uh',
#        'mm',
#        'ah',
#        'er',
#        'eh',
#        'mhm',
#        'hm',
#        'ha',
#        'huh',
#        'uhuh'
#        # Do these count?
#        #'ooh',
#        #'oh',
#        )



# (defun cleanup-trees (trees)
#   ;; The functions I wrote shouldn't be destructive, but make copies, just in case
#   (setf trees (mapcar 'copy-tree trees))
#   (setf trees (mapcar 'remove-edited-layers trees))
#   (setf trees (mapcar 'remove-disfluencies trees))
#   (setf trees (remove-if 'null trees))
#   (setf trees (remove '((INTJ)) trees :test 'equalp))
#   )

file = sys.argv[1]

for line in open(file):
    line = line[:-1]

    # Get rid of the punctuations that cause trouble (we're not going to use them anyway)
    line = line.replace('(. .)', '')
    line = line.replace('(, ,)', '')
    line = line.replace('(. ?)', '')
    line = line.replace('(. !)', '')
    line = line.replace('(: -)', '')
    line = line.replace('(`` ``)', '')
    line = line.replace("('' '')", '')
    line = line.replace('(: ...)', '')


    # WE COULD DO THESE WITHIN LISP... IT MIGHT BE A LITTLE SAFER... BUT PERHAPS NOT NECESSARY
    # Remove the disfluency markers:
    line = line.replace('(RM (-DFL- \[) )', '')
    line = line.replace('(IP (-DFL- \+) )', '')
    line = line.replace('(RS (-DFL- \]) )', '')

    # Remove the end sentence (?) markers
    line = line.replace('(-DFL- E_S)', '')
    line = line.replace('(-DFL- N_S)', '')

    # We could also remove this sort of stuff...
    #line = line.replace('(INTJ (UH um) )', '')
    #line = line.replace('(INTJ (UH uh) )', '')

    line = re.sub('\(INTJ \(UH um\) +\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH uh\) +\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( +\(INTJ \(UH Uh-huh\) +\)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( +\(INTJ \(UH Uh huh\) +\)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( +\(INTJ \(UH Um-hum\) +\)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( +\(INTJ \(UH Huh-uh\) +\)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( +\(INTJ \(UH huh\) +\)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( +\(INTJ \(UH Uh-uh\) +\)\)', '', line, flags=re.IGNORECASE)


    line = re.sub('\(INTJ \(UH Uh-huh\) +\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH Uh huh\) +\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH Um-hum\) +\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH Huh-uh\) +\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH huh\) +\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH duh\) +\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH Uh-uh\) +\)', '', line, flags=re.IGNORECASE)


    # Is this safe to do?
    line = re.sub('\(UH um\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(UH uh\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(UH huh\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(UH uh-huh\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(UH huh-uh\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(UH uh-oh\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(UH huh-huh\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(UH huh-\)', '', line, flags=re.IGNORECASE)

    line = re.sub('\( \(INTJ \(\S* uh-huh\) +\)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( \(INTJ \(UH Hm\)   \)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH Hm\) \)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( \(INTJ \(UH Ah\)   \)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(UH Ah\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\( \(INTJ \(UH Ha-ha\)   \)\)', '', line, flags=re.IGNORECASE)
    line = re.sub('\(INTJ \(UH ha\) \)', '', line, flags=re.IGNORECASE)
    

    # Here's one typo we can fix!
    line = line.replace('(TYPO (DT uh) )', '(DT a)', line)
    
    

    # Escape single quotes (these show up in possessives and contractions)
    # We only need this if we're actually going to read it into Lisp
    #line = line.replace("'", "\\'")
    # Remove anything that looks like (VB .)... these are errors?
    line = re.sub("\([A-Z]+ \,\)", "", line)
    # Remove ambiguous labels like... VBN|VBD 
    line = re.sub("\|[A-Z]+ ", " ", line)

    # Still need to get rid of the carets...
    line = line.replace('^', '')

    print line

