# for i in {1..18}
# do
#     rm -rf ./extract/gson_${i}_buggy/test/test_for_methodcallfrequency/GetMCF4SingleTestcase.sh
#     rm -rf ./extract/gson_${i}_buggy/test/test_for_methodcallfrequency/GetMCF4SingleTestsuite.sh
#     cp -r ./Patch4Experiment/test/test_for_methodcallfrequency/GetMCF4SingleTestcase.sh ./extract/gson_${i}_buggy/test/test_for_methodcallfrequency/GetMCF4SingleTestcase.sh
#     cp -r ./Patch4Experiment/test/test_for_methodcallfrequency/GetMCF4SingleTestsuite.sh ./extract/gson_${i}_buggy/test/test_for_methodcallfrequency/GetMCF4SingleTestsuite.sh
# done

# for i in {1..18}
# do
#     rm -rf ./extract/gson_${i}_buggy/test/test_for_RFC/GetMutantDis.py
#     cp -r ./Patch4Experiment/test/test_for_RFC/GetMutantDis.py ./extract/gson_${i}_buggy/test/test_for_RFC/GetMutantDis.py

#     rm -rf ./extract/gson_${i}_buggy/test/test_for_RFC/GetClassDis.py
#     cp -r ./Patch4Experiment/test/test_for_RFC/GetClassDis.py ./extract/gson_${i}_buggy/test/test_for_RFC/GetClassDis.py

#     rm -rf ./extract/gson_${i}_buggy/test/test_for_RFC/GetMutantDis4Class.py
#     cp -r ./Patch4Experiment/test/test_for_RFC/GetMutantDis4Class.py ./extract/gson_${i}_buggy/test/test_for_RFC/GetMutantDis4Class.py

#     rm -rf ./extract/gson_${i}_buggy/test/test_for_RFC/GetClassDis4Class.py
#     cp -r ./Patch4Experiment/test/test_for_RFC/GetClassDis4Class.py ./extract/gson_${i}_buggy/test/test_for_RFC/GetClassDis4Class.py
# done

# for i in {1..18}
# do
#     cp -r ./Patch4Experiment/test/test_for_FL ./extract/gson_${i}_buggy/test/test_for_FL
    
#     # rm -rf ./extract/gson_${i}_buggy/test/test_for_FL/GetData.sh
#     # cp -r ./Patch4Experiment/test/test_for_FL/GetData.sh ./extract/gson_${i}_buggy/test/test_for_FL/GetData.sh

#     # rm -rf ./extract/gson_${i}_buggy/test/test_for_FL/SuspiciousnessCalculatorRFC.py
#     # cp -r ./Patch4Experiment/test/test_for_FL/SuspiciousnessCalculatorRFC.py ./extract/gson_${i}_buggy/test/test_for_FL/SuspiciousnessCalculatorRFC.py

#     # rm -rf ./extract/gson_${i}_buggy/test/test_for_FL/SuspiciousnessCalculator.py
#     # cp -r ./Patch4Experiment/test/test_for_FL/SuspiciousnessCalculator.py ./extract/gson_${i}_buggy/test/test_for_FL/SuspiciousnessCalculator.py
# done

for i in {1..18}
do
    rm -rf ./extract/gson_${i}_buggy/test/test_for_method/GetAllMethods.sh
    cp -r ./Patch4Experiment/test/test_for_method/GetAllMethods.sh ./extract/gson_${i}_buggy/test/test_for_method/GetAllMethods.sh

    rm -rf ./extract/gson_${i}_buggy/test/test_for_method/GetCovfMethods.py
    cp -r ./Patch4Experiment/test/test_for_method/GetCovfMethods.py ./extract/gson_${i}_buggy/test/test_for_method/GetCovfMethods.py

    rm -rf ./extract/gson_${i}_buggy/test/test_for_method/GetRFCMethods.py
    cp -r ./Patch4Experiment/test/test_for_method/GetRFCMethods.py ./extract/gson_${i}_buggy/test/test_for_method/GetRFCMethods.py

    rm -rf ./extract/gson_${i}_buggy/test/test_for_method/GetMethod4Buggylines.py
    cp -r ./Patch4Experiment/test/test_for_method/GetMethod4Buggylines.py ./extract/gson_${i}_buggy/test/test_for_method/GetMethod4Buggylines.py
done

# for i in {1..18}
# do
#     rm -rf ./extract/gson_${i}_buggy/test/test_for_filestatistic
#     cp -r ./Patch4Experiment/test/test_for_filestatistic ./extract/gson_${i}_buggy/test/test_for_filestatistic
# done