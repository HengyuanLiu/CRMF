#!usr/bin/python3

import pandas as pd

def get_mutantclass(mutant):
    mutant = mutant.split(":")
    MutantNo = int(mutant[0])
    if "@" in mutant[4]:
        Class = mutant[4].split("@")[0]
        Method = mutant[4].split("@")[1]
    else:
        Class = mutant[4]
        Method = ""
    return MutantNo, Class, Method

testMap_df = pd.read_csv("./testMap.csv", header=0)
killMap_df = pd.read_csv("./killMap.csv", header=0)
covMap_df = pd.read_csv("./covMap.csv", header=0)
kill_df = pd.read_csv("./kill.csv", header=0,index_col=0)
mutants_fp = open("./mutants.log", mode="r")
mutants = mutants_fp.readlines()
mutants_fp.close()

testsuites = testMap_df["TestNo"].to_list()

fp = open("../../../test_for_testsuites/failtestcases.txt",mode='r')
failtestcasesName = fp.read()
fp.close()
failtestcasesName = failtestcasesName.strip().split("\n")
failtestsuitesName = [failtestcaseName.split("::")[0] for failtestcaseName in failtestcasesName]
testMap = {
    testMap_df.loc[i, "TestName"]:testMap_df.loc[i, "TestNo"] for i in testMap_df.index 
}
failtestsuites = [testMap[failtestsuiteName] for failtestsuiteName in failtestsuitesName]

MutantDis = pd.DataFrame(index=kill_df.index,columns=["Class", "Method"]+testsuites)

for mutant in mutants:
    MutantNo, Class, Method = get_mutantclass(mutant)
    if MutantNo in MutantDis.index:
        MutantDis.loc[MutantNo, "Class"] = Class
        MutantDis.loc[MutantNo, "Method"] = Method

MutantDis[testsuites] = 0
MutantDis[failtestsuites] = 1

for i in killMap_df.index:
    TestNo = killMap_df.loc[i, "TestNo"]
    MutantNo = killMap_df.loc[i, "MutantNo"]
    if MutantNo in MutantDis.index and TestNo in failtestsuites:
        MutantDis.loc[MutantNo, TestNo] = 0
    elif MutantNo in MutantDis.index:
        MutantDis.loc[MutantNo, TestNo] = 1
    else:
        pass

MutantDis["MutantDis"] = MutantDis[testsuites].sum(axis=1)
MutantDis.to_csv("./MutantDis.csv")

