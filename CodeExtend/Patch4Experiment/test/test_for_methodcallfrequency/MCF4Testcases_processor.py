#!/usr/bin/python3
# The processor for extract the frequency of method

import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def string_spliter(string, sep):
    string = string.split(sep)
    return [string_item.strip() for string_item in string if string_item.strip() != ""]

# MCF raw data read
fp = open("./MCF4Testcases.txt",mode="r")
MCF_raw = fp.read()
fp.close()

# Get fail testcases
fp = open("../test_for_testsuites/failtestcases.txt",mode="r")
failtestcases = fp.readlines()
fp.close()
failtestcases = [failtestcase.strip() for failtestcase in failtestcases]

MCF_df = pd.DataFrame(columns=["Testsuite", "Testcase", "Method", "TestResult", "CallFrequency"])

# MCF_raw = MCF_raw.split()
# MCF_raw = [MCF_entity for MCF_entity in MCF_raw if MCF_entity.strip() != ""]

MCF_raw = string_spliter(MCF_raw, "------------------------------------------------------")
for MCF_entity in MCF_raw:

    # MCF_entity = MCF_entity.split("\n")
    # MCF_entity = [MCF_line for MCF_line in MCF_entity if MCF_line.strip() != ""]

    MCF_entity = string_spliter(MCF_entity, "\n")

    S_Testcase = MCF_entity[0]

    S_Testsuite = S_Testcase.split("::")[0]

    if S_Testcase in failtestcases:
        S_TestResult = "FAIL"
    else:
        S_TestResult = "PASS"

    S_mcf = MCF_entity[-1]
    S_mcf = string_spliter(S_mcf[1:-1], ",")

    for method_mcf in S_mcf:
        S_Method, S_CallFrquency = method_mcf.split("=")

        MCF_df = MCF_df.append({
            "Testsuite": S_Testsuite,
            "Testcase": S_Testcase, 
            "Method": S_Method, 
            "TestResult": S_TestResult, 
            "CallFrequency": S_CallFrquency
        }, ignore_index=True)

MCF_df.to_csv("./MCF4Testcases.csv", index=False)
