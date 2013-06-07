
FILES=`ls *.wv*`

#echo $FILES

for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  #cat $f
  /net/ayesha/usr1/home/rsingh/bin/shorten -x $f $f.sph
done
