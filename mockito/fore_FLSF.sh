#!/bin/bash
n=1
Method=""
for line in `cat FLSF/ef-mockito$1.txt | tr -d '\r' `
do
	if [[ $(($n%2)) == 1 ]];then
		Method=$line
	else
		if [[ $line -gt 20 ]];then
			str=1
		else
			str1=`echo 3.14^$line | bc`
			str2=`echo "scale=10;3.14^(-1*$line)" | bc`
			# str1=${str1//\\/}
			# str1=`echo $str1 | sed 's/ //g'`
			# str2=${str2//\\/}
			# str2=`echo $str2 | sed 's/ //g'`
			# echo "$str1-$str2="
			
			cha=`echo "scale=10;$str1-$str2" | bc`
			he=`echo "scale=10;$str1+$str2" | bc`
			# cha=${cha//\\/}
			# cha=`echo $cha | sed 's/ //g'`
			# he=${he//\\/}
			# he=`echo $he | sed 's/ //g'`
			# echo "$cha"
			# echo "$str1+$str2=$he"
			str=`echo "scale=10;$cha/$he" | bc`
			if [[ $str =~ ^\..* ]];then
				str="0$str"
			fi
		fi
		echo $Method ${str} >> e_FLSF/ef-mockito$1.txt
	fi
	n=$(($n+1))
done

for line in `cat FLSF/ep-mockito$1.txt | tr -d '\r' `
do
	if [[ $(($n%2)) == 1 ]];then
		Method=$line
	else
		if [[ $line -gt 20 ]];then
			str=1
		else
			str1=`echo 3.14^$line | bc`
			str2=`echo "scale=10;3.14^(-1*$line)" | bc`
			# str1=${str1//\\/}
			# str1=`echo $str1 | sed 's/ //g'`
			# str2=${str2//\\/}
			# str2=`echo $str2 | sed 's/ //g'`
			# echo "$str1-$str2="
			
			cha=`echo "scale=10;$str1-$str2" | bc`
			he=`echo "scale=10;$str1+$str2" | bc`
			# cha=${cha//\\/}
			# cha=`echo $cha | sed 's/ //g'`
			# he=${he//\\/}
			# he=`echo $he | sed 's/ //g'`
			# echo "$cha"
			# echo "$str1+$str2=$he"
			str=`echo "scale=10;$cha/$he" | bc`
			if [[ $str =~ ^\..* ]];then
				str="0$str"
			fi
		fi
		echo $Method ${str} >> e_FLSF/ep-mockito$1.txt
	fi
	n=$(($n+1))
done