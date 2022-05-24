#!usr/bin/python3

import pandas as pd

def method2class(method):
    method = method.split(".")[:-1]
    return ".".join(method)

MCF_df = pd.read_csv("../test_for_methodcallfrequency/MCF4Testsuites.csv", header=0)
fp=open("../test_for_class/allclasses.txt",mode='r')
all_classes = fp.readlines()
fp.close()
all_classes = [c.strip() for c in all_classes]

Class_Covf = []
Method_Covf = MCF_df[MCF_df["TestResult"]=="FAIL"]
for method_covf in Method_Covf["Method"]:
    class_covf = method2class(method_covf)
    if class_covf in all_classes:
        Class_Covf.append(method2class(method_covf))

Class_Covf = list(set(Class_Covf))
fp = open("./covfclasses.txt",mode="w")
fp.write("\n".join(Class_Covf))
fp.close()
