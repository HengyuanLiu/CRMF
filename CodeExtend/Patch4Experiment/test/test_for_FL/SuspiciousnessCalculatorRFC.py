import numpy as np
import pandas as pd
import math

def suspiciousnesscalculator(method, MCF_data, RFC_classes):
    # print(MCF_data.shape)
    N_testsuite_f = MCF_data.loc[MCF_data["TestResult"]=="FAIL",["Testsuite","TestResult"]].drop_duplicates(keep="first").shape[0]
    N_testsuite_p = MCF_data.loc[MCF_data["TestResult"]=="PASS",["Testsuite","TestResult"]].drop_duplicates(keep="first").shape[0]
    # print(N_testsuite_f)
    # print(N_testsuite_p)

    MCF_method = MCF_data[MCF_data["Method"]==method]
    N_method_cov_f = MCF_method[MCF_method["TestResult"]=="FAIL"].shape[0]
    N_method_cov_p = MCF_method[MCF_method["TestResult"]=="PASS"].shape[0]

    N_method_uncov_f = N_testsuite_f - N_method_cov_f
    N_method_uncov_p = N_testsuite_p - N_method_cov_p

    # print("ef:{},ep:{},nf:{},np:{}".format(N_method_cov_f, N_method_cov_p, N_method_uncov_f, N_method_uncov_p))

    # Jaccard = ef/(ef+nf+ep)
    Jaccard = N_method_cov_f / (N_method_cov_f + N_method_uncov_f + N_method_cov_p)

    # Ochiai = ef/sqrt((ef+nf)*(ef+ep))
    if N_method_cov_f == 0:
        Ochiai = 0
    else:
        Ochiai =  N_method_cov_f / math.sqrt((N_method_cov_f + N_method_uncov_f) * (N_method_cov_f + N_method_cov_p))

    # Dstar = ef^3/(ep+nf)
    if (N_method_cov_p + N_method_uncov_f) == 0:
        # Dstar = 200
        Dstar = np.Inf
    else:
        Dstar = N_method_cov_f ** 3 / (N_method_cov_p + N_method_uncov_f)

    # op2 = ef - ep /(ep+np+1)
    op2 = N_method_cov_f - N_method_cov_p / (N_method_cov_p + N_method_uncov_p + 1)

    # Tarantula = (ef/(ef+nf))/((ef/ef+nf)+(ep/ep+np))
    if N_method_cov_f == 0 and N_method_cov_p == 0:
        Tarantula = 0
    else:
        Tarantula = (N_method_cov_f/(N_method_cov_f + N_method_uncov_f)) / ((N_method_cov_f/(N_method_cov_f + N_method_uncov_f)) + (N_method_cov_p / (N_method_cov_p + N_method_uncov_p)))

    # FLSF
    alpha = 0.6
    if MCF_method.loc[MCF_method["TestResult"]=="FAIL", "CallFrequency"].empty and MCF_method.loc[MCF_method["TestResult"]=="PASS", "CallFrequency"].empty:
        flsf = -1
    else:
        F_method_cov_f = (alpha * MCF_method.loc[MCF_method["TestResult"]=="FAIL", "CallFrequency"]).map(math.tanh).sum()
        F_method_cov_p = (alpha * MCF_method.loc[MCF_method["TestResult"]=="PASS", "CallFrequency"]).map(math.tanh).sum()
        flsf= (F_method_cov_f/N_testsuite_f) / ( (F_method_cov_f/N_testsuite_f) + (F_method_cov_p/N_testsuite_p) )

    # MFSF
    if '.'.join(method.split('.')[:-1]) in RFC_classes:
        lam = 0.5
        F_testsuite_f = MCF_data.loc[MCF_data["TestResult"]=="FAIL", "CallFrequency"].sum()
        F_testsuite_p = MCF_data.loc[MCF_data["TestResult"]=="PASS", "CallFrequency"].sum()
        F_method_cov_f = MCF_method.loc[MCF_method["TestResult"]=="FAIL", "CallFrequency"].sum()
        F_method_cov_p = MCF_method.loc[MCF_method["TestResult"]=="PASS", "CallFrequency"].sum()
        N_testsuite = MCF_data.shape[0]
        N_method_cov = MCF_method.shape[0]
        mfsf = (F_method_cov_f/F_testsuite_f) / ((F_method_cov_p+1)/(F_testsuite_p)) * math.log(N_testsuite/(N_method_cov+lam))
    else:
        mfsf = 0

    # print("""
    # Jaccard:{}
    # Ochiai:{}
    # Dstar:{}
    # op2:{}
    # Tarantula:{}
    # FLSF:{}
    # MFSF:{}
    # """.format(Jaccard,Ochiai,Dstar,op2,Tarantula,flsf,mfsf))

    suspiciousness_dict = {
        "Jaccard":Jaccard,
        "Ochiai":Ochiai,
        "Dstar":Dstar,
        "op2":op2,
        "Tarantula":Tarantula,
        "FLSF":flsf,
        "MFSF":mfsf
    }
    return suspiciousness_dict

MCF_data = pd.read_csv("./MCF4Testsuites.csv", header=0)

RFC_fp = open("./RFC_classes.txt", mode="r")
RFC_classes = RFC_fp.readlines()
RFC_fp.close()
RFC_classes = [c.strip() for c in RFC_classes]

methods = list(set(MCF_data["Method"].to_list()))

MethodNo = [i for i in range(len(methods))]
suspiciousness_formula = ["Jaccard","Ochiai","Dstar","op2","Tarantula","FLSF","MFSF"]
Suspiciousness = pd.DataFrame(index=MethodNo, columns=["Method"]+suspiciousness_formula)

Suspiciousness["Method"] = methods
Suspiciousness=Suspiciousness.sort_values(by="Method")
# method = methods[0]
# suspiciousness_dict = suspiciousnesscalculator(method, MCF_data)
# print(list(suspiciousness_dict.values()))
for method in methods:
    suspiciousness_dict = suspiciousnesscalculator(method, MCF_data, RFC_classes)
    Suspiciousness.loc[Suspiciousness["Method"]==method,suspiciousness_formula]=list(suspiciousness_dict.values())

# print(Suspiciousness.head())

Suspiciousness.to_csv("./SuspiciousnessRFC.csv",index=False)

MethodRank = Suspiciousness.copy()
for formula in suspiciousness_formula:
    # MethodRank[formula] = MethodRank[formula].rank(axis=0,method="average",ascending=False).astype("int")
    MethodRank[formula] = MethodRank[formula].rank(axis=0,method="average",ascending=False)


# print(MethodRank.head())
MethodRank.to_csv("./MethodRankRFC.csv",index=False)



