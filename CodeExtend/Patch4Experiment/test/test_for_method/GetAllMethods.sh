#!/bin/bash
rm -rf all_methods.txt
cd ../../target/classes

cp -r ../../../../Patch4Experiment/push ./push

for class in `cat ../../test/test_for_class/allclasses.txt`;
# for class in `cat ../../test/test_for_class/allclasses.txt | tr -d '\r' `;
do
    # echo $class
    java -classpath .:/home/rs/Work/CRMF/Compress/extract/compress_${1}_buggy/target/test-classes:/home/rs/Work/CRMF/Compress/extract/compress_${1}_buggy/target/classes:/home/rs/Work/Junit/junit4-r4.12/target/junit-4.12.jar:/home/rs/.m2/repository/javassist/javassist/3.12.1.GA/javassist-3.12.1.GA.jar:/home/rs/.m2/repository/net/bytebuddy/byte-buddy/1.8.20/byte-buddy-1.8.20.jar:/home/rs/.m2/repository/net/bytebuddy/byte-buddy-agent/1.8.20/byte-buddy-agent-1.8.20.jar:/home/rs/.m2/repository/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar:/home/rs/.m2/repository/org/tukaani/xz/1.8/xz-1.8.jar:/home/rs/.m2/repository/org/objenesis/objenesis/2.6/objenesis-2.6.jar:/home/rs/.m2/repository/com/github/luben/zstd-jni/1.3.3-1/zstd-jni-1.3.3-1.jar:/home/rs/.m2/repository/org/brotli/dec/0.1.2/dec-0.1.2.jar:/home/rs/.m2/repository/org/powermock/powermock-module-junit4/1.7.3/powermock-module-junit4-1.7.3.jar:/home/rs/.m2/repository/org/powermock/powermock-api-mockito/1.7.3/powermock-api-mockito-1.7.3.jar:/home/rs/.m2/repository/org/powermock/powermock-api-mockito-common/1.7.3/powermock-api-mockito-common-1.7.3.jar:/home/rs/.m2/repository/org/powermock/powermock-core/1.7.3/powermock-core-1.7.3.jar:/home/rs/.m2/repository/org/powermock/powermock-api-support/1.7.3/powermock-api-support-1.7.3.jar:/home/rs/.m2/repository/org/mockito/mockito-core/1.10.19/mockito-core-1.10.19.jar:/home/rs/.m2/repository/org/powermock/powermock-reflect/1.7.3/powermock-reflect-1.7.3.jar -Dencoding=UTF-8 push.Getmethod $class >> ../../test/test_for_method/all_methods_temp.txt
done
cd ../../test/test_for_method/
sort -u all_methods_temp.txt > all_methods.txt
rm -rf all_methods_temp.txt
