# test extract the all classes of gson 5
rm -rf allclasses.txt
function read_dir(){
    for file in `ls $1` #注意此处这是两个反引号，表示运行系统命令
    do
            if [ -d $1"/"$file ] #注意此处之间一定要加上空格，否则会报错
            then
                read_dir $1"/"$file
            else
            if [[ $file =~ .*\.java$ ]];then
                str=${1//\//\.}
                str=$str"."$file
                str=${str%\.java*}
                if [[ $1 =~ org.mockito ]];then
                    str=${str#*src.main.java.org.mockito.}
                elif [[ $1 =~ org.jfree ]]; then
                    str=${str#*src.main.java.org.jfree.}
                elif [[ $1 =~ org.joda.time ]]; then
                    str=${str#*src.main.java.org.joda.time.}
                elif [[ $1 =~ org.apache.commons.math3 ]]; then
                    str=${str#*src.main.java.org.apache.commons.math3.}
                elif [[ $1 =~ org.apache.commons.math ]]; then
                    str=${str#*src.main.java.org.apache.commons.math.}
                elif [[ $1 =~ org.apache.commons.lang3 ]]; then
                    str=${str#*src.main.java.}
                    # str=${str#*src.main.java.org.apache.commons.lang3.}
                elif [[ $1 =~ org.apache.commons.lang ]]; then
                    str=${str#*src.main.java.}
                    # str=${str#*src.main.java.org.apache.commons.lang.}
                elif [[ $1 =~ com.google.gson ]]; then
                    str=${str#*src.main.java.}
                    # str=${str#*src.main.java.org.apache.commons.gson.}
                fi
                echo $str #在此处处理文件即可
            fi
            fi
    done
} 
# read_dir ../../src/main/java/org/apache/commons/gson
#读取第一个参数
if [[ $1 == "mockito" ]];then
    read_dir ../../src/main/java/org/mockito >> allclasses.txt
elif [[ $1 == "chart" ]]; then
    read_dir ../../src/main/java/org/jfree >> allclasses.txt
elif [[ $1 == "time" ]]; then
    read_dir ../../src/main/java/org/joda/time >> allclasses.txt
elif [[ $1 == "math" ]]; then
    if [[ $2 -gt 35 ]];then
        read_dir ../../src/main/java/org/apache/commons/math >> allclasses.txt
    else
        read_dir ../../src/main/java/org/apache/commons/math3 >> allclasses.txt
    fi
elif [[ $1 == "lang" ]]; then
    if [[ $2 -gt 39 ]];then
        read_dir ../../src/main/java/org/apache/commons/lang >> allclasses.txt
    else
        read_dir ../../src/main/java/org/apache/commons/lang3 >> allclasses.txt
    fi
elif [[ $1 == "gson" ]]; then
    read_dir ../../gson/src/main/java/com/google/gson >> allclasses.txt
fi