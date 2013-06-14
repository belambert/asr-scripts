#$ -S /bin/sh
source ~/.bashrc

if [ $# -ne 1 ]; then
    echo "Usage: $0 <ctl file>"
    exit -1
fi
  
ctl_file=$1

tagger_location="$HOME/software/stanford-postagger"
pos_model="$HOME/final_models/spost-left5words,suffix(3)-all.tagger"

counter=0
total=`wc -l $ctl_file`

for file in `cat $ctl_file`; do

    folder=`dirname $file`

    # Keep a counter of how many we've done
    let counter=counter+1
    if [ $((counter%100)) -eq 0 ]; then
	echo "POS tagged $counter of $total"
    fi

    # Unzip the n-best list if it's zipped, but keep the
    # zipped version (i.e. use gunzip -c)
    unzipped_file=$folder/`basename $file .gz`
    gunzip -c $file > $unzipped_file
    
    # Keep track of the filenames
    txt_file=$unzipped_file.txt
    conditioned_file=$unzipped_file.txt.conditioned
    tokenized_file=$unzipped_file.txt.conditioned.tokenized
    tagged_file=$unzipped_file.tagged
    conll_file=$unzipped_file.tagged.conll
    parsed_file=$unzipped_file.parsed
    collapsed_file=$unzipped_file.parsed.collapsed

    # Convert the n-best list from Sphinx format to something that the POS tagger can use...
    ~/thesis/scripts/parser/nbest-to-txt.sh $unzipped_file > $txt_file

    # Remove the um's, punctuation, and all that jazz
    ~/thesis/scripts/condition-source-text.sh $txt_file > $conditioned_file

    # Tokenize
    ~/thesis/scripts/tokenize.sh $conditioned_file > $tokenized_file

    # Run the POS tagger
    java -mx4000m -classpath $tagger_location/stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger \
	-model $pos_model \
	-textFile $tokenized_file \
	-sentenceDelimiter newline \
	-tokenize false \
	> $tagged_file 2> $tagged_file.err

    # Check that the number of lines match!  If not, fail!
    orig_line_count=`wc -l $txt_file | awk '{print $1}'`
    tagged_line_count=`wc -l $tagged_file | awk '{print $1}'`
    if [[ $orig_line_count -ne $tagged_line_count ]]; then
	echo "Line counts don't match!! $orig_line_count $tagged_line_count $txt_file $tagged_file"
	exit -1
    fi

    # Convert from POS to conll
    ~/thesis/scripts/parser/pos-to-conll.sh $tagged_file > $conll_file

    # Do a sanity check
    conll_line_count=`./count-conll-sentences.sh $conll_file`
    if [[ $orig_line_count -ne $conll_line_count ]]; then
	echo "Line counts don't match!! $orig_line_count $conll_line_count $txt_file $conll_file"
	exit -1
    fi
    
    # Run the parser
    ~/thesis/scripts/parser/run-maltparser.sh $conll_file 2> $parsed_file.err

    # Collapse the dependencies
    ~/thesis/scripts/parser/collapse-conll-file.sh $parsed_file > $collapsed_file

    # Delete everything we don't want to keep
    rm $unzipped_file
    rm $txt_file
    rm $conditioned_file
    rm $tokenized_file
    rm $tagged_file
    rm $conll_file
    rm $tagged_file.err
    rm $parsed_file.err   
    # Gzip everything we *do* want to keep
    # The -f is to 'force' and so overwrite something if it's already there
    gzip -f $parsed_file
    gzip -f $collapsed_file

done
        


