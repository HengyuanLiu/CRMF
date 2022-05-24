# process the testcase level result to testsuite level

import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


MCF_testcases = pd.read_csv("./MCF4Testcases.csv", header=0)

testsuites = list(set(MCF_testcases["Testsuite"].tolist()))

MCF_testsuites = pd.DataFrame(columns=["Testsuite", "Method", "TestResult", "CallFrequency"])
for testsuite in testsuites:
    MCF_testsuite = MCF_testcases[MCF_testcases["Testsuite"]==testsuite]

    TestResults = list(set(MCF_testsuite["TestResult"].tolist()))
    if "FAIL" in TestResults:
        TestResult = "FAIL"
    else:
        TestResult = "PASS"
        
    methods = list(set(MCF_testsuite["Method"].tolist()))
    for method in methods:
        if MCF_testsuite[MCF_testsuite["Method"]==method].shape[0] != 0:
            MCF_testsuites = MCF_testsuites.append({
                "Testsuite":testsuite,
                "Method":method,
                "TestResult":TestResult, 
                "CallFrequency":MCF_testsuite.loc[MCF_testsuite["Method"]==method, "CallFrequency"].sum()
            }, ignore_index=True)
MCF_testsuites.to_csv("./MCF4Testsuites.csv",index=False)

    






