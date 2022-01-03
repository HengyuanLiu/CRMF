#!/bin/bash
#该脚本需要输入两个参数，参数1：程序错误版本号，参数2：是在pass还是fail测试用例集中的覆盖频率TF
pro=chart
for method in `cat susMethod/susMethod$1.txt | tr -d '\r'`
do
	printf "$method  "
	k=0
	sum=0
	mk=0
	ave=0
	ans=0
	for line in `cat Yichuli/${pro}$1-$2TS.txt | tr -d '\r'`
	do
		if [[  $line =~ ^.*\=.* ]];then

			sum=$(($sum+${line#*=}))
			# echo $sum
			if [[ ${line%=*} = $method ]] ; then
				mk=${line#*=}
				# echo $mk
				k=$(($k+1))
				
			fi
		else
			if [ $sum -gt 0 ];then
				# echo $sum
				# echo $mk $sum
				# t=$(($mk/$sum))
				t=$(echo "scale=10; $mk / $sum" | bc )
				# echo $t
				# echo $t
				# ave=$(($ave+$t))
				ave=$(echo "scale=10; $ave + $t" | bc )
				
			fi
			sum=0
			mk=0

		fi
	done
	if [ $sum -gt 0 ];then
				# echo $sum
				# echo $mk $sum
				# t=$(($mk/$sum))
				t=$(echo "scale=10; $mk / $sum" | bc )
				# echo $t
				# echo $t
				# ave=$(($ave+$t))
				ave=$(echo "scale=10; $ave + $t" | bc )
				# echo $ave
			fi
			

	if [ $k -gt 0 ]; then
		# echo $(($ave/$k))
		# echo $method
		# echo $mk $sum
		# echo $ave $k 
		ans=$(echo "scale=10; $ave / $k" | bc )
	fi
	printf "$ans\n"
	sum=0
	mk=0
done

