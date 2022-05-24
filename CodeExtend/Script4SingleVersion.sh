# $1 version
basepath=$(cd `dirname $0`; pwd)

# ############################################################################################
# #   Project-Version Extraction
# ############################################################################################
# echo ---------------------------------------------------------------------------------------
# echo Project-Version Extraction
# echo ---------------------------------------------------------------------------------------

# version="${1}b"
# defects4j checkout -p Gson -v $version -w ./extract/gson_$1_buggy

# if [[ $? -ne 0 ]]; then
#     echo FAILURE!!!
#     exit
# fi

# ############################################################################################
# #   Run Preparation
# ############################################################################################
# echo ---------------------------------------------------------------------------------------
# echo Run Preparation
# echo ---------------------------------------------------------------------------------------

# cd ./extract/gson_$1_buggy

# defects4j test

# if [[ $? -ne 0 ]]; then
#     echo FAILURE!!!
#     exit
# fi

# cd $basepath

# ############################################################################################
# #   Set Patch
# ############################################################################################
# echo ---------------------------------------------------------------------------------------
# echo Set Patch
# echo ---------------------------------------------------------------------------------------

# cp -r ./Patch4Experiment/com/test ./extract/gson_$1_buggy/gson/src/main/java/com/test
# rm -rf ./extract/gson_$1_buggy/gson/src/main/resources
# if [ ! -d "./extract/gson_$1_buggy/gson/src/main/resources/" ]; then
#     mkdir -p ./extract/gson_$1_buggy/gson/src/main/resources/
# fi
# cp -r ./Patch4Experiment/resources/META-INF ./extract/gson_$1_buggy/gson/src/main/resources/META-INF
# cp -r ./Patch4Experiment/test ./extract/gson_$1_buggy/test

###########################################################################################
#   Experiment
###########################################################################################
echo ---------------------------------------------------------------------------------------
echo Start Experiment
echo ---------------------------------------------------------------------------------------

cd ./extract/gson_$1_buggy

# # Pom Modifier

# cd ./test/pom_modifier

# python3 ./pom_modifier.py

# cd ../..

# # Get all testsuites, testcases and fail testcases
# echo ---------------------------------------------------------------------------------------
# echo Get All Testsuites
# echo ---------------------------------------------------------------------------------------

# cd ./test/test_for_testsuites

# bash ./GetTestsuites.sh
# bash ./GetTestcases.sh
# bash ./GetFailTestcases.sh

# cd ../..

# # Get all classes
# echo ---------------------------------------------------------------------------------------
# echo Get All Class Name
# echo ---------------------------------------------------------------------------------------

# cd ./test/test_for_class

# bash ./getAllclassName.sh gson $1

# cd ../..

# # Get true buggy method
# echo ---------------------------------------------------------------------------------------
# echo Get True Buggy Method
# echo ---------------------------------------------------------------------------------------

# # cd ./test/test_for_buggylines

# # bash get_buggy_lines.sh Gson $1 ./

# # cd ../..

# cd ./test/test_for_method

# cp ../../test/test_for_buggylines/Gson-${1}.buggy.lines ./buggy_lines.txt
# python3 ./GetMethod4Buggylines.py
# # rm -rf ./buggy_lines.txt

# cd ../..

# # Get mcf
# echo ---------------------------------------------------------------------------------------
# echo Get Method Call Frequency
# echo ---------------------------------------------------------------------------------------

# cd ./test/test_for_methodcallfrequency

# # # bash ./MvnCompile.sh

# # if [ `grep -c "BUILD SUCCESS" ./MvnCompile-log.txt` -ne '0' ];then
# #     echo "Mvn Compile Success!"
# # else
# #     echo "Mvn Compile Fail!"
# #     echo $1 >> ${basepath}/VersionCompileFailed.txt
# #     exit
# # fi

# bash ./GetMCF4Testcases.sh $1

# if [ ! -f "./TimeoutTestsuite.txt" ];then
#     echo "All testsuites are executed with time limit 8s!"
# else
#     echo "There are some time out testsuites!"
#     echo $1 >> ${basepath}/VersionWithTimeout.txt
# fi

# python3 ./MCF4Testcases_processor.py
# python3 ./MCFTestcases2MCFTestsuites.py

# cd ../..

# # Get covf classes
# echo ---------------------------------------------------------------------------------------
# echo Get Class Coverd by Fail Testsuites
# echo ---------------------------------------------------------------------------------------

# cd ./test/test_for_class

# python3 ./getClassCovftestsuites.py

# cd ../..

# # RFC
# echo ---------------------------------------------------------------------------------------
# echo Conduct RFC
# echo ---------------------------------------------------------------------------------------

# cd ./test/test_for_RFC

# # bash ./GetMAResult_byClass.sh Gson $1

# # if [[ $? -ne 0 ]]; then
# # echo Gson $1 MA FAil!
# # else
# # echo Gson $1 MA Get!
# # fi 

# if [ -d "./MAResults" ]; then
#     for class in `ls ./MAResults`
#     do
#         echo ${class}
#         cd ./MAResults/${class}
#         python3 ../../GetMutantDis4Class.py 2>/dev/null
#         if [[ $? -ne 0 ]]; then
#             echo "FAILURE!!!\(${class}\)"
#         fi
#         cd ../..
#     done
#     python3 ./GetClassDis4Class.py
# else
#     python3 ./GetMutantDis.py
#     python3 ./GetClassDis.py
# fi

# cd ../..

# # FL
# echo ---------------------------------------------------------------------------------------
# echo Conduct FL
# echo ---------------------------------------------------------------------------------------

# cd ./test/test_for_FL

# bash ./GetData.sh

# python3 ./SuspiciousnessCalculatorRFC.py
# python3 ./SuspiciousnessCalculator.py

# cd ../..

# # Get all methods, covf methods, RFC methods
# echo ---------------------------------------------------------------------------------------
# echo Get All Method Name
# echo ---------------------------------------------------------------------------------------

# cd ./test/test_for_method

# bash ./GetAllMethods.sh

# python3 ./GetCovfMethods.py

# python3 ./GetRFCMethods.py

# cd ../..

# Get file statistic
echo ---------------------------------------------------------------------------------------
echo Get File Statistic
echo ---------------------------------------------------------------------------------------

cd ./test/test_for_filestatistic

python3 ./GetAllSrcLineCount.py
if [ $? -ne 0 ]; then
    echo Fail on Version ${1}
fi

cd ../..
