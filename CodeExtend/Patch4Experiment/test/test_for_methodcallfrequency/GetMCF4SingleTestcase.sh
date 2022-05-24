# $1 version $2 testsuite $3 testcase
timeout 30s java -Xms128M -Xmx512M -javaagent:/home/rs/Work/CRMF/Gson/extract/gson_${1}_buggy/gson/target/gson-0.0-SNAPSHOT.jar -classpath /home/rs/Work/CRMF/Gson/extract/gson_${1}_buggy/target/test-classes:/home/rs/Work/CRMF/Gson/extract/gson_${1}_buggy/target/classes:/home/rs/Work/Junit/junit4-r4.12/target/junit-4.12.jar:/home/rs/.m2/repository/javassist/javassist/3.12.1.GA/javassist-3.12.1.GA.jar:/home/rs/.m2/repository/net/bytebuddy/byte-buddy/1.8.20/byte-buddy-1.8.20.jar:/home/rs/.m2/repository/net/bytebuddy/byte-buddy-agent/1.8.20/byte-buddy-agent-1.8.20.jar:/home/rs/.m2/repository/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar:/home/rs/.m2/repository/org/tukaani/xz/1.8/xz-1.8.jar:/home/rs/.m2/repository/org/objenesis/objenesis/2.6/objenesis-2.6.jar:/home/rs/.m2/repository/com/github/luben/zstd-jni/1.3.3-1/zstd-jni-1.3.3-1.jar:/home/rs/.m2/repository/org/brotli/dec/0.1.2/dec-0.1.2.jar:/home/rs/.m2/repository/org/powermock/powermock-module-junit4/1.7.3/powermock-module-junit4-1.7.3.jar:/home/rs/.m2/repository/org/powermock/powermock-api-mockito/1.7.3/powermock-api-mockito-1.7.3.jar:/home/rs/.m2/repository/org/powermock/powermock-api-mockito-common/1.7.3/powermock-api-mockito-common-1.7.3.jar:/home/rs/.m2/repository/org/powermock/powermock-core/1.7.3/powermock-core-1.7.3.jar:/home/rs/.m2/repository/org/powermock/powermock-api-support/1.7.3/powermock-api-support-1.7.3.jar:/home/rs/.m2/repository/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.jar:/home/rs/.m2/repository/org/powermock/powermock-reflect/1.7.3/powermock-reflect-1.7.3.jar org.junit.runner.JUnitCore $2 -m $3 >> ./test/test_for_methodcallfrequency/MCF4Testcases.txt 2>&1
if [ $? == 124 ]; then
    echo "Time Out ! Skip the Rest Execution of Testsuite : ${2}::${3}"  >> ./test/test_for_methodcallfrequency/TimeoutTestcase.txt
    exit
fi
