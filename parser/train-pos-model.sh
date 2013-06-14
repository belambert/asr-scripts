#!/bin/sh

# Additional documentation on the parameters and features for this POS tagger can be found
# at the following Web pages:
# Parameters:              http://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/tagger/maxent/MaxentTagger.html
# Feature extraction:      http://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/tagger/maxent/ExtractorFrames.html
# Rare feature extraction: http://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/tagger/maxent/ExtractorFramesRare.html


arch="left5words,suffix(3)"

lang="english"

# Parser setup/location
classpath="$HOME/software/stanford-postagger/stanford-postagger.jar"

train="$HOME/data/swb-mrg/swb.txt"
train_ref="$HOME/data/swb-mrg/swb.pos"

# Evaluate the model on the training and testing data
train_output="$train.tagged.all"
test_output="$test.tagged.all"

echo $arch    
model="$HOME/data/swb-mrg/spost-$arch-all.tagger"

# Do the actual training of the model
echo "Training model..."
java -mx2000m -classpath $classpath edu.stanford.nlp.tagger.maxent.MaxentTagger \
    -model $model \
    -trainFile $train_ref \
    -arch $arch \
    -tagSeparator _ \
    -lang $lang

echo "Tagging and evaluating the training data"
java -mx2000m -cp $classpath edu.stanford.nlp.tagger.maxent.MaxentTagger \
    -model $model \
    -textFile $train \
    -sentenceDelimiter newline \
    -tokenize false \
    > $train_output

$HOME/thesis/scripts/parser/evaluate-pos-tags.sh $train_ref $train_output

if [ -n "$test" -a -n "$test_ref" ]; then
    echo "Tagging and evaluating the testing data"
    java -mx2000m -cp $classpath edu.stanford.nlp.tagger.maxent.MaxentTagger \
	-model $model \
	-textFile $test \
	-sentenceDelimiter newline \
	-tokenize false \
	> $test_output
    $HOME/thesis/scripts/parser/evaluate-pos-tags.sh $test_ref $test_output -verbose
fi


