#!/usr/bin/env bash
# $1 version
# entity granularity: method
# test granularity: test suite
rm -rf ./MCF4Testsuites.txt
rm -rf ./TimeoutTestsuite.txt
for testsuite in `cat ../test_for_testsuites/testsuites.txt`;
do 
    echo ------------------------------------------------------ >> ./MCF4Testsuites.txt
    echo $testsuite >> ./MCF4Testsuites.txt
    cd ../../
    # java -javaagent:/home/rs/Work/CRMF/Gson/extract/gson_${1}_buggy/target/commons-gson-0.0-SNAPSHOT.jar -classpath /home/rs/Work/CRMF/Gson/extract/gson_${1}_buggy/target/test-classes:/home/rs/Work/CRMF/Gson/extract/gson_${1}_buggy/target/classes:/home/rs/Work/Junit/junit4-r4.12/target/junit-4.12.jar:/home/rs/.m2/repository/javassist/javassist/3.12.1.GA/javassist-3.12.1.GA.jar:/home/rs/.m2/repository/net/bytebuddy/byte-buddy/1.8.20/byte-buddy-1.8.20.jar:/home/rs/.m2/repository/net/bytebuddy/byte-buddy-agent/1.8.20/byte-buddy-agent-1.8.20.jar:/home/rs/.m2/repository/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar:/home/rs/.m2/repository/org/tukaani/xz/1.8/xz-1.8.jar org.junit.runner.JUnitCore $testsuite >> ./test/test_for_methodcallfrequency/MCF.txt 2>&1
    bash ./test/test_for_methodcallfrequency/GetMCF4SingleTestsuite.sh $1 $testsuite
    cd ./test/test_for_methodcallfrequency
done