#!/bin/bash
#需要输入4个参数，前两个时版本号起始和末尾，第三是日志时间戳，比如1 5 09171923。第4个参数表示开始的测试类的名字，比如RetryRunnerTest

# #适用于math37前的版本
i=$1
flag=0
for line in ` cat math${1}-${2}-output${3}.txt | tr -d '\r'`
do
	if [ $i -gt $2 ];then
		echo $i
		break
	fi
	touch Yichuli/math${i}.txt
	
			
	if [[ $line = $4 ]];then
		if [[ $flag -eq 0 ]];then
			flag=1
			echo $4 >> Yichuli/math${i}.txt

		elif [[ $flag -eq 1 ]];then
			i=$(($i+1))
			echo $4 >> Yichuli/math${i}.txt
		fi
	else

		if [[ $line =~ org.apache.*\=[0-9].* ]];then
			echo ${line#*org.apache.commons.math3.} >> Yichuli/math${i}.txt

		elif [[ ! $line =~ org.apache.* ]];then
			echo >> Yichuli/math${i}.txt
			echo $line >> Yichuli/math${i}.txt
			
		fi
	fi
done 

# #适用于math37及37之后的版本
# i=$1
# flag=0
# for line in ` cat math${1}-${2}-output${3}.txt | tr -d '\r'`
# do
# 	if [ $i -gt $2 ];then
# 		echo $i
# 		break
# 	fi
# 	touch Yichuli/math${i}.txt
	
			
# 	if [[ $line = $4 ]];then
# 		if [[ $flag -eq 0 ]];then
# 			flag=1
# 			echo ${4#*org.apache.commons.math.} >> Yichuli/math${i}.txt

# 		elif [[ $flag -eq 1 ]];then
# 			i=$(($i+1))
# 			echo ${4#*org.apache.commons.math.} >> Yichuli/math${i}.txt
# 		fi
# 	else

# 		if [[ $line =~ org.apache.*\=[0-9].* ]];then
# 			echo ${line#*org.apache.commons.math.} >> Yichuli/math${i}.txt

# 		elif [[ ! $line =~ ^org.apache.*\=M[0-9].* ]];then
# 			echo >> Yichuli/math${i}.txt
# 			echo ${line#*org.apache.commons.math.} >> Yichuli/math${i}.txt
			
# 		fi
# 	fi
# done 