
FILES=`ls *.wv*`

for f in $FILES; do
  echo "Processing $f file..."
  /net/ayesha/usr1/home/rsingh/bin/shorten -x $f $f.sph
done
