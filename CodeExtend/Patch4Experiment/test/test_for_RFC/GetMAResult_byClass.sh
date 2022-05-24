# $1 projects $2 version

echo ---------------------
start_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "MA start time $start_time"

pid="$1" 
bid="$2b"
projectpath=~/Work/D4J_repositoy/${pid,,}_$2_buggy
echo defects4j checkout -p $1 -v $bid -w $projectpath
defects4j checkout -p $1 -v $bid -w $projectpath

basepath=$(cd `dirname $0`; pwd)
echo $basepath
cd $projectpath

for line in `cat $basepath/../test_for_class/covfclasses.txt | tr -d '\r'`
do
    echo $line
    tmp_path="$basepath/../test_for_RFC/MAResults/$line/"
    if [ ! -d "$tmp_path" ]; then
        mkdir -p $tmp_path
    fi

    echo $line > $tmp_path/export_class.txt
    defects4j mutation -i $tmp_path/export_class.txt

    if [[ $? -ne 0 ]]; then
        echo FAILURE!!!
        echo $line > $basepath/../test_for_RFC/classesMAFail.txt
    else
        cp ${projectpath}/mutants.log ${tmp_path}/mutants.log
        cp ${projectpath}/killMap.csv ${tmp_path}/killMap.csv
        cp ${projectpath}/covMap.csv ${tmp_path}/covMap.csv
        cp ${projectpath}/testMap.csv ${tmp_path}/testMap.csv
        cp ${projectpath}/kill.csv ${tmp_path}/kill.csv
    fi
done

end_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "MA end time $end_time"
echo ---------------------

# rm -rf $projectpath