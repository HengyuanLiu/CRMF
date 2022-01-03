#!/bin/bash

if [[ -z $1 ]] || [[ -z $2 ]] || [[ -z $3 ]];then
	echo "请输入三个参数，程序名，起始版本号，终止版本号"
else
	prom=$1

	for i in `seq $2 $3`
	do 
		if [[ -e ../${prom}/${prom}_${i}_buggy ]] ;then 
			./dealwithAns.sh ${prom} $i  
			python sort.py ${prom} $i
		fi
	done 
fi