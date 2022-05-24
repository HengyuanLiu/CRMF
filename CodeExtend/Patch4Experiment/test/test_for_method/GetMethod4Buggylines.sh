#!/bin/bash
for line in `cat ../test_for_buggylines/Gson-${1}.buggy.lines | tr -d '\r' `
do
	if [[ $line =~  .*\#[0-9]+\# ]]; then
		filename=${line%%\#*}
		len_number=${line#*\#}
		len_number=${len_number%\#*}
		echo `bash ./getmethodname4buggyline.sh ../../gson/src/main/java/$filename $len_number` >> ./buggy_methods_temp.txt
	fi
done
for line in  `cat ./buggy_methods_temp.txt | tr -d '\r'` 
do
	echo $line >> ./temp.txt
done
sort -u ./temp.txt > ./buggy_methods.txt
rm -rf ./temp.txt
rm -rf ./buggy_methods_temp.txt

