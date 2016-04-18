#!/usr/bin/python


import sys
import re

file = sys.argv[1]

#id_file = True
id_file = False

mode = "none"
#mode = "all"
#mode = "strip_parens"
#mode = "strip_contents"

for line in open(file):
    line = line[:-1]
    
    first_paren = line.rfind("(")
    trans = line[:first_paren]
    id = line[first_paren+1:-1]

    if len(trans) > 0:
        printp = True
        if "((" in trans and "))" in trans:
            if mode == "none":
                #print line
                # 1.  Don't print this line at all...
                printp=False
            elif mode == "all":
                # 2. Just print it all anyway
                printp=True
            elif mode == "strip_parens":
                # 3. Remove just the parens...
                trans = trans.replace("((", "")
                trans = trans.replace("))", "")
                printp=True
            elif mode == "strip_contents":
                # 4. Remove everything between the parens
                trans = re.sub("\(\(.*\)\)", "", trans)
                printp=True
            else:
                raise

        # Check if there are any remaining parens
        if printp and ( "(" in trans or ")" in trans ):
            sys.stderr.write("Spurious parens?: %s\n"%trans)

        # Common:
        trans = re.sub(' +',' ', trans)
        trans = trans.strip()

        line = "%s (%s)"%(trans, id)

        if printp:
            if id_file:
                print id
            else:
                print line
    

