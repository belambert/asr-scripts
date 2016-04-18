#!/usr/bin/python

import subprocess, os

memory='14000m'

algs=['2planar', 'covnonproj', 'covproj', 'nivreeager', 'nivrestandard', 'planar', 'stackeager', 'stacklazy', 'stackproj']

file_location='/usr0/home/belamber/data/swb-mrg/parser_eval'

train_model_p=False
#train_model_p=True

#metric='LAS'
#metric='UAS'
metric='LA'

os.chdir(file_location)

train_file="%s/swb-train.conll"%file_location
test_file="%s/swb-test.conll"%file_location

for alg in algs:
    print "-----------------------------------------------------"
    print "Attempting to train/parse using models with algorithm: %s"%alg
    model="swb-basic-linear-train.%s"%alg
    error_output="%s/%s.err"%(file_location, model)
    print model

    if train_model_p:
        # Train the model
        if not os.path.isfile('%s.mco'%model):
            print "Training model..."
            shell_string="java -Xmx%s -jar ~/software/maltparser/maltparser-1.7.1.jar -c %s -i %s -m learn -l liblinear -a %s -grl 'root' -nr false 2> %s"%(memory, model, train_file, alg, error_output)
            output=subprocess.call(shell_string, shell=True)
        else:
            print "Model already exists... using existing model."

    # Now that we've trained a model... we should run it on the respective test file...
    # print "Running parser..."
    parsed_file='parsed-test-%s.parsed'%alg
    # parsing_errors='parsed-test-%s.err'%alg
    # shell_string="java -Xmx%s -jar ~/software/maltparser/maltparser-1.7.1.jar -c %s -i %s -m parse -o %s 2> %s"%(memory, model, test_file, parsed_file, parsing_errors)
    # output=subprocess.call(shell_string, shell=True)

    print "Evaluating file..."
    eval_file='%s.eval'%parsed_file
    shell_string="java -Xmx2000m -jar ~/software/MaltEval-20081119/lib/MaltEval.jar -g %s -s %s --Metric %s > %s"%(test_file, parsed_file, metric, eval_file)
    output=subprocess.call(shell_string, shell=True)
    #grep "Row mean" $eval_file
                


