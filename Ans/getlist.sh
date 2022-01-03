#!/bin/bash

#参数：程序名
max=0
if [[ $1 == "math" ]];then
	max=106
elif [[ $1 == "chart" ]]; then
	max=26
elif [[ $1 == "time" ]]; then
	max=27
elif [[ $1 == "mockito" ]]; then
	max=38
elif [[ $1 == "lang" ]]; then
	max=63
else
	echo "参数输入错误,请输入正确的程序名"
	exit 1
fi



for i in `seq 1 $max `
do
	if [[ -f finalAns/$1/${1}${i}-ans.txt ]];then
		echo $1$i  >> ${1}list.txt
	fi
done