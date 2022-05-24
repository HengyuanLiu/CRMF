#!/bin/bash
#需要输出1个参数，参数1指定需要提取方法及对应行数的文件
temp=${1#*java/}
echo $temp
temp=${temp%.java*}
echo $temp
temp=${temp//\//\.}
echo $temp
echo ---------------------------------------------
for line in `cat ${1} | tr -d '\r' `
do
	i=$(($i+1))
	echo line:$i
	echo $line
	if [[ $line =~ .*\(.*\).*\{ ]] || [[ $line =~ .*public.*\(.*\, ]] || [[ $line =~ .*private.*\(.*\, ]] || [[ $line =~ .*protected.*\(.*\, ]];then
		if  [[ ! $line =~ .*\/\/.* ]] &&[[ ! $line =~ .*\ if\ .* ]] && [[ ! $line =~ .*\ for\ .*\(.* ]] && [[ ! $line =~ .*\}.*\{ ]] && [[ ! $line =~ .*\*.* ]] ;then
			echo $line
			a=${line%(*}
			
			methodName=`echo $a |awk -F"  *"  '{print $NF}'`
			if [[ $methodName =~ ^[a-z][a-zA-Z0-9]+$ ]] ;then
				echo "${temp}.${methodName}"
			fi
		fi
	fi
done