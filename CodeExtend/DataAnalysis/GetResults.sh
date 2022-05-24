result_dir="./Results"
data_dir="../extract"
for i in {1..18}
do
    if [ ! -d "${result_dir}/gson_${i}_buggy" ]; then
        mkdir ${result_dir}/gson_${i}_buggy
    fi

    # File Statistic
    cp ${data_dir}/gson_${i}_buggy/test/test_for_filestatistic/FileLineCount.txt ${result_dir}/gson_${i}_buggy/FileLineCount.txt

    # Test Data
    cp ${data_dir}/gson_${i}_buggy/test/test_for_testsuites/testsuites.txt ${result_dir}/gson_${i}_buggy/testsuites.txt
    cp ${data_dir}/gson_${i}_buggy/test/test_for_testsuites/testcases.txt ${result_dir}/gson_${i}_buggy/testcases.txt

    # FL Result
    cp ${data_dir}/gson_${i}_buggy/test/test_for_FL/MethodRank.csv ${result_dir}/gson_${i}_buggy/MethodRank.csv
    cp ${data_dir}/gson_${i}_buggy/test/test_for_FL/MethodRankRFC.csv ${result_dir}/gson_${i}_buggy/MethodRankRFC.csv

    # True Buggy Data
    cp ${data_dir}/gson_${i}_buggy/test/test_for_buggylines/Gson-${i}.buggy.lines ${result_dir}/gson_${i}_buggy/buggy_lines.txt
    cp ${data_dir}/gson_${i}_buggy/test/test_for_method/buggy_methods.txt ${result_dir}/gson_${i}_buggy/buggy_methods.txt

    # RFC Result
    cp ${data_dir}/gson_${i}_buggy/test/test_for_method/all_methods.txt ${result_dir}/gson_${i}_buggy/all_methods.txt
    cp ${data_dir}/gson_${i}_buggy/test/test_for_method/covf_methods.txt ${result_dir}/gson_${i}_buggy/covf_methods.txt
    cp ${data_dir}/gson_${i}_buggy/test/test_for_method/RFC_methods.txt ${result_dir}/gson_${i}_buggy/RFC_methods.txt
done
