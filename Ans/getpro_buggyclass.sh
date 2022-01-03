#!/bin/bash

#参数1个：程序名

prom=$1
cd ../$prom

for line in `cat ${prom}_buggylines-new.txt | tr -d '\r'`
do
	if [[ $line =~ ${prom}[0-9].* ]];then
		echo $line >> ${prom}_buggyclass.txt
	else
		echo ${line%.*} >> ${prom}_buggyclass.txt
	fi
done