#!/bin/bash
#需要输出2个参数，参数1指定需要提取方法及对应行数的文件,参数2表示错误语句行数
IFS=$'\n'
breakflag="No"
# i=0
for line in `cat ${1} | tr -d '\r' `
do
	i=$(($i+1))
	# echo line:$i
	# echo $line
	# if [[ $line =~ .*\(.*\).*\{ ]] || [[ $line =~ .*public.*\(.*\, ]] || [[ $line =~ .*private.*\(.*\, ]] || [[ $line =~ .*protected.*\(.*\, ]];then
	if [[ $line =~ .*public[^=]*\(.* ]] || [[ $line =~ .*private[^=]*\(.* ]] || [[ $line =~ .*protected[^=]*\(.* ]] || [[ $line =~ .*static[^=]*\(.* ]] || [[ $line =~ .*int[^=]*\(.* ]];then
		if [[ ! $line =~ .*\*.* ]] && [[ ! $line =~ .*\}.*\{ ]]; then
		# if [[ $line =~ .*\(.*\).*\{ ]] ; then
		# if [[ $line =~ .*\(.*\) ]] ; then
		# if  [[ ! $line =~ .*\/\/.* ]] &&[[ ! $line =~ .*if.* ]] && [[ ! $line =~ .*\ for\ .*\(.* ]] && [[ ! $line =~ .*\}.*\{ ]] && [[ ! $line =~ .*\*.* ]] ;then
			methodName=`echo ${line%(*} |awk -F"  *"  '{print $NF}'`
			# echo $methodName
			# echo $line

			if [[ $line =~ .*\[.*\].* ]];then
				line=${line//\[/\\\[}
				line=${line//\]/\\\]}
			fi
			# if [[ $line =~ .*\?.* ]]; then
			# 	line=${line//\?/\\\?}
			# fi
			# if [[ $line =~ .*\<.*\>.* ]]; then
			# 	line=${line//\</\\\<}
			# 	line=${line//\>/\\\>}
			# fi
			# methodline=$line
			# echo $1
			n=`sed -n "/$line/=" ${1}`
			# echo @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
			# echo $methodline
			# echo $n
			# echo $line

			n_num=`echo $n | awk '{print NF}'`
			n1=$n
			if [[ $n_num -gt 1 ]];then
				tempi=1
				n_tempi=`echo $n1 | awk -v VAR=$tempi '{print $VAR}'`
				n=$n_tempi
				
				while [[ $n_tempi -le $2 ]] && [[ $tempi -le $n_num ]]
				do
					n=$n_tempi
					tempi=$(($tempi + 1))
					
					n_tempi=`echo $n1 | awk -v VAR=$tempi '{print $VAR}'`
				done				
			fi

			if [[ $line =~ .*\( ]] && [[ ! $line =~ .*\(.*\) ]]; then
				# echo ------
				# echo `sed -n -e ${n}p $1`
				# n_add_1=$((${n}+1))
				# n=777
				# echo expr ${n[0]} \+ 1
				n_add_1=`expr ${n[0]} \+ 1`
				# echo $n_add_1
				# echo `sed -n -e ${n_add_1}p $1`
				# echo ------

				n=$n_add_1
				line=$(echo `sed -n -e ${n_add_1}p $1`)

				# echo ??????????????????????????????????????
				# echo $n
				# echo $line
				# echo ??????????????????????????????????????
				if [[ $line =~ .*\[.*\].* ]];then
					line=${line//\[/\\\[}
					line=${line//\]/\\\]}
				fi
			fi

			# echo ***********************************
			# echo $n
			
			# while [ [$tempi] -lg $2 ]
			# echo $n | awk '{print $1}'

			# n=`sed -n "/$line/=" ${1}`
			# echo $n
			num_left=`echo $line | awk -F "{" '{print NF-1}'`
			num_right=`echo $line | awk -F "}" '{print NF-1}'`
			m=$n
			
			cat ${1} | awk "NR > $n" ${1} | while read name
			do
				if [[ $num_left == $num_right ]];then
					# echo "n=$n m=$m"
					if [[ $2 -ge $n ]] && [[ $2 -le $m ]];then
						classname=${1//\//\.}
						classname=${classname#*java\.}
						classname=${classname%java*}
						if [[ ! -z $methodName ]];then
							# echo @@@@@@@@@@@@@@@@@@@@@@
							echo ${classname}${methodName}
							breakflag="Yes"
						fi
					fi
					# echo $m
					break
				fi
				temp=`echo $name | awk -F "{" '{print NF-1}'`
				num_left=$(($num_left+$temp))
				temp=`echo $name | awk -F "}" '{print NF-1}'`
				num_right=$(($num_right+$temp))
				# echo "num_left=$num_left  num_right=$num_right"
				
				m=$(($m+1))
				# m=`expr $m + 1 `

				# echo $m
				# echo "---$name"
			done
			
			# str=`grep -n $line ${1}`
			# echo ${str%:*}
		fi
	else
		if [[ $line =~ .*throws.*\{.* ]]; then
			if [[ ! $line =~ .*\*.* ]] && [[ ! $line =~ .*\}.*\{ ]]; then
				# echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
				b=${line%(*}
				# echo $b

				# echo $methodline
				methodName=`echo ${methodline%(*} |awk -F"  *"  '{print $NF}'`
				# echo $methodName
				# echo $line
				if [[ $line =~ .*\[.*\].* ]];then
					line=${line//\[/\\\[}
					line=${line//\]/\\\]}
				fi
				# if [[ $line =~ .*\?.* ]]; then
				# 	line=${line//\?/\\\?}
				# fi
				# if [[ $line =~ .*\<.*\>.* ]]; then
				# 	line=${line//\</\\\<}
				# 	line=${line//\>/\\\>}
				# fi
				# echo $1

				# echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				# echo 
				# echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				n=`sed -n "/$line/=" ${1}`
				# echo ------------------?????????
				method_n=`sed -n "/${methodline}/=" ${1}`
				# echo $methodline
				# echo "n:"
				# echo $n
				# echo "method_n:"
				# echo $method_n

				method_n_num=`echo $method_n | awk '{print NF}'`
				method_n1=$method_n
				if [[ $method_n_num -gt 1 ]];then
					method_tempi=1
					method_n_tempi=`echo $method_n1 | awk -v VAR=$method_tempi '{print $VAR}'`
					method_n=$method_n_tempi
					
					while [[ $method_n_tempi -le $2 ]] && [[ $method_tempi -le $method_n_num ]]
					do
						method_n=$method_n_tempi
						method_tempi=$(($method_tempi + 1))
						
						method_n_tempi=`echo $method_n1 | awk -v VAR=$method_tempi '{print $VAR}'`
					done				
				fi
				# echo ***********************************
				# echo $method_n

				for n_i in $n;
				do
					if [[ $n_i -gt $method_n ]]; then
						n=$n_i
						break
					fi
				done
				# echo $line
				# echo ????????????????????????????????????????????????????????????
				n_num=`echo $n | awk '{print NF}'`
				n1=$n
				# echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				# echo 
				# echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				if [[ $n_num -gt 1 ]];then
					tempi=1
					n_tempi=`echo $n1 | awk -v VAR=$tempi '{print $VAR}'`
					n=$n_tempi
					
					while [[ $n_tempi -le $2 ]] && [[ $tempi -le $n_num ]]
					do
						n=$n_tempi
						tempi=$(($tempi + 1))
						
						n_tempi=`echo $n1 | awk -v VAR=$tempi '{print $VAR}'`
					done				
				fi
				
				# while [ [$tempi] -lg $2 ]
				# echo $n | awk '{print $1}'

				# n=`sed -n "/$line/=" ${1}`
				# echo $n
				num_left=`echo $line | awk -F "{" '{print NF-1}'`
				num_right=`echo $line | awk -F "}" '{print NF-1}'`
				m=$n
				
				cat ${1} | awk "NR > $n" ${1} | while read name
				do
					# echo $num_left $num_right
					# echo "n=$n m=$m"
					if [[ $num_left == $num_right ]];then
						# echo ??????????????????
						# echo $method_n
						# echo $methodline
						# echo "n=$n m=$m"
						if [[ $2 -ge $n ]] && [[ $2 -le $m ]];then
							classname=${1//\//\.}
							classname=${classname#*java\.}
							classname=${classname%java*}
							if [[ ! -z $methodName ]];then
								# echo ~~~~~~~~~~~~~~~~~~~~~
								echo ${classname}${methodName}
								breakflag="Yes"
								# echo
								# echo 
							fi
						fi
						# echo $m
						break
					fi
					temp=`echo $name | awk -F "{" '{print NF-1}'`
					num_left=$(($num_left+$temp))
					temp=`echo $name | awk -F "}" '{print NF-1}'`
					num_right=$(($num_right+$temp))
					# echo "num_left=$num_left  num_right=$num_right"
					
					m=$(($m+1))
					# m=`expr $m + 1 `

					# echo $m
					# echo "---$name"
				done
				
				# str=`grep -n $line ${1}`
				# echo ${str%:*}
			fi
		fi
	fi

	if [[ breakflag = "Yes" ]]; then
		break
	fi
done