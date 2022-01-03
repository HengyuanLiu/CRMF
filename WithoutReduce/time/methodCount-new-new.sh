#!/bin/bash

# for method in `cat susMethod/susMethod$1.txt | tr -d '\r'`
# do 

# 	
# done

for method in `cat susMethod/susMethod$1.txt | tr -d '\r'`
do 
	method=${method}=
	echo ${method%=*} `grep -c ^$method Yichuli/time$1.txt` >> MC/MC-time$1.txt
	ef1=`grep -c ^$method Yichuli/time$1-failTS.txt`
	if [[ $ef1 -ge 1 ]];then
		echo ${method%=*} `grep -c ^$method Yichuli/time$1-failTS.txt` >> SBFL/ef-time$1.txt
		# # echo "${method%=*} 1" >> SBFL/ef-time$1.txt
		str=`grep ^$method Yichuli/time$1-failTS.txt `
		array=(${str//\ / })
		sum=0
		n=0
		for i in ${array[@]}
		do
			sum=$(($sum+${i#*=}))
			n=$(($n+1))
		done
		ef_c=$(($sum/$n))
		echo "${method%=*} $ef_c" >> FLSF/ef-time$1.txt
	else
		echo "${method%=*} 0" >> SBFL/ef-time$1.txt
		echo "${method%=*} 0" >> FLSF/ef-time$1.txt
	fi

	ep1=`grep -c ^$method Yichuli/time$1-passTS.txt`
	if [[ $ep1 -ge 1 ]];then
		echo ${method%=*} `grep -c ^$method Yichuli/time$1-passTS.txt` >> SBFL/ep-time$1.txt
		# # echo "${method%=*} 1" >> SBFL/ep-time$1.txt
		str=`grep ^$method Yichuli/time$1-passTS.txt `
		array=(${str//\ / })
		sum=0
		n=0
		for i in ${array[@]}
		do
			sum=$(($sum+${i#*=}))
			n=$(($n+1))
		done
		ep_c=$(($sum/$n))
		echo "${method%=*} $ep_c" >> FLSF/ep-time$1.txt
	else
		echo "${method%=*} 0" >> SBFL/ep-time$1.txt
		echo "${method%=*} 0" >> FLSF/ep-time$1.txt
	fi

done

