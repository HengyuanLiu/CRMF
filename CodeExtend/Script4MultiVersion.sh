if [ ! -d ./log ]; then
  mkdir -p ./log
fi

# 1..18

# 1-18 to mvn compile
for i in {1..18}
do
    echo --------
    echo $i
    # echo $i >> ./VersionMAGot.txt
    # bash ./Script4SingleVersion.sh $i >> ./log/gson_${i}.txt 2>&1
    bash ./Script4SingleVersion.sh $i
    if [[ $? -ne 0 ]]; then
      echo FAILURE!!!
    fi
    echo --------
done

echo Run Over!

# bash ./Script4SingleVersion.sh 1 >> ./log/gson_1.txt 2>&1