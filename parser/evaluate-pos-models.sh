#!/bin/sh

# Parser setup/location
classpath="$HOME/software/stanford-postagger/stanford-postagger.jar"

#train="$HOME/swb-mrg/swb-train.txt"
#train_ref="$HOME/swb-mrg/swb-train.pos"

test="$HOME/swb-mrg/swb-test.txt"
test_ref="$HOME/swb-mrg/swb-test.pos"

#train="$HOME/swb-mrg/swb.txt"
#train_ref="$HOME/swb-mrg/swb.pos"


models="english-bidirectional-distsim.tagger  english-caseless-left3words-distsim.tagger  english-left3words-distsim.tagger  wsj-0-18-bidirectional-nodistsim.tagger  wsj-0-18-caseless-left3words-distsim.tagger  wsj-0-18-left3words-distsim.tagger"

# Evaluate the model on the training and testing data
train_output="$train.eval.tagged"
test_output="$test.eval.tagged"

for model in $models; do
    echo $model

    model="$HOME/software/stanford-postagger/models/$model"

    if [ -n "$train" -a -n "$train_ref" ]; then
	echo "Tagging and evaluating the training data"
	java -mx2000m -cp $classpath edu.stanford.nlp.tagger.maxent.MaxentTagger \
	    -model $model \
	    -textFile $train \
	    -sentenceDelimiter newline \
	    -tokenize false \
	    > $train_output	
	$HOME/thesis/scripts/parser/evaluate-pos-tags.sh $train_ref $train_output
    fi

    if [ -n "$test" -a -n "$test_ref" ]; then
	echo "Tagging and evaluating the testing data"
	java -mx2000m -cp $classpath edu.stanford.nlp.tagger.maxent.MaxentTagger \
	    -model $model \
	    -textFile $test \
	    -sentenceDelimiter newline \
	    -tokenize false \
	    > $test_output
	$HOME/thesis/scripts/parser/evaluate-pos-tags.sh $test_ref $test_output
    fi
done

