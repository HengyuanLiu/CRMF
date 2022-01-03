#!/bin/bash

#参数2个： 程序名，版本号
if [[ -z $1 ]] || [[  -z $2 ]] ;then
	echo "请输入参数2个： 程序名，版本号"
else	


	OLD_IFS=$IFS
	IFS=$'\n'
	lastone=""
	theone=""
	sum=0
	ni=0
	ans=0
	danger=""
	if [[ ! -e finalAns/${1} ]];then
		mkdir finalAns/${1}
	fi

	for line in `cat ${1}/${1}${2}.txt | tr -d '\r'`
	do
		if [[ $line =~ faultline ]]	;then
			continue
		else
			if [[ $line =~ .*No:.* ]];then
				IFS=$OLD_IFS
				arr=($line)
				lastone=$theone
				theone=${arr[1]}
				# printf "${arr[1]} "
				IFS=$'\n'
			else
				if [[ ! $line == "-" ]];then
					if [[ $lastone == $theone ]] || [[ $lastone == "" ]] ;then
						sum=$(($sum+$line))
						ni=$(($ni+1))
						if [[ $theone == $danger ]];then
							danger=""
						fi
					else
						if [[ ! $danger == "" ]];then
							echo "$danger 2000" >> finalAns/${1}/${1}${2}.txt
							danger=""
						fi
						if [[ $ni -gt 0 ]];then
							ans=`echo "scale=2;$sum/$ni" | bc`
							# echo $sum $ni
							echo $lastone $ans >> finalAns/${1}/${1}${2}.txt
						fi
						sum=0
						ni=0
						sum=$(($sum+$line))
						ni=$(($ni+1))
					fi
				else
					if [[ ! $lastone == $theone ]] || [[ $lastone == "" ]];then
						if [[ ! $danger == "" ]];then
							echo "$danger 2000" >> finalAns/${1}/${1}${2}.txt
							danger=""
						elif [[ ! $lastone == "" ]];then
						
							ans=`echo "scale=2;$sum/$ni" | bc`
							# echo $sum $ni
							echo $lastone $ans >> finalAns/${1}/${1}${2}.txt
						# echo $theone $line >> finalAns/${1}/${1}${2}.txt
						fi
						danger=$theone
						sum=0
						ni=0
					# else
						# echo $lastone $line >> finalAns/${1}/${1}${2}.txt
					fi
				fi
			fi
		fi
	done


	if [[ ! $danger == "" ]];then
		echo "$danger 2000" >> finalAns/${1}/${1}${2}.txt
		danger=""
	else
		ans=`echo "scale=2;$sum/$ni" | bc`
		# echo $sum $ni
		echo $lastone $ans >> finalAns/${1}/${1}${2}.txt
	fi
	# n=0
	# for line in `cat finalAns/${1}/${1}${2}.txt | tr -d '\r'`
	# do
	# 	if [[ $line =~ .*-.* ]];then
fi