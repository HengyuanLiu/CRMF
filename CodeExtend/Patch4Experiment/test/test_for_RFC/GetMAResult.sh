# $1 projects $2 version
pid="$1" 
bid="$2b"
tmppath=~/Work/D4J_repositoy/${pid,,}_$2_buggy
echo defects4j checkout -p $1 -v $bid -w $tmppath
defects4j checkout -p $1 -v $bid -w $tmppath

basepath=$(cd `dirname $0`; pwd)
echo $basepath
cd $tmppath

defects4j mutation -i $basepath/../test_for_class/covfclasses.txt

cp ${tmppath}/mutants.log ${basepath}/mutants.log
cp ${tmppath}/killMap.csv ${basepath}/killMap.csv
cp ${tmppath}/covMap.csv ${basepath}/covMap.csv
cp ${tmppath}/testMap.csv ${basepath}/testMap.csv
cp ${tmppath}/kill.csv ${basepath}/kill.csv

# rm -rf $tmppath