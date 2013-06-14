#$ -S /bin/sh
source ~/.bashrc

if [ $# -ne 1 ]; then
  echo "Usage: `basename $0` <file to tag>"
  exit -1
fi

file=$1
#tagger_location="$HOME/software/stanford-postagger"
tagger_location="$HOME/software/stanford-postagger"
#pos_model="$HOME/pos-tagger/models/left3words_suffix3_eng_swb_all.tagger"
#pos_model="$HOME/final_models/spost-left5words,suffix(3)-all.tagger"
#pos_model="$HOME/final_models/spost-periods-left5words,suffix(3)-all.tagger"


#pos_model="$HOME/data/swb-mrg/spost-left5words,suffix(3)-all.tagger"
pos_model="$HOME/final_models/spost-left5words,suffix(3)-all.tagger"

tagged_file=`dirname $file`/`basename $file .txt`.tagged

java -mx4000m -classpath $tagger_location/stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger \
    -model $pos_model \
    -textFile $file \
    -sentenceDelimiter newline \
    -tokenize false \
    > $tagged_file 2> $tagged_file.err

#-sentenceDelimiter newline \

orig_line_count=`wc -l $file | awk '{print $1}'`
tagged_line_count=`wc -l $tagged_file | awk '{print $1}'`
if [[ $orig_line_count -ne $tagged_line_count ]]; then
    echo "Line counts don't match!! $orig_line_count  $tagged_line_count"
    exit -1
fi
        


