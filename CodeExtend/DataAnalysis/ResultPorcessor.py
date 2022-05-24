#### process the FL result ####

import os
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def judge4method(m, c):
    m = m.split(".")
    c = c.split('.')
    if (len(m) - len(c)) == 1:
        return True
    else:
        return False

Project = "Gson"
data_cols = ["Jaccard","Ochiai","Dstar","op2","Tarantula","FLSF","MFSF"]
EXAM_df = pd.DataFrame(columns=["Project","Version","Method"]+data_cols)
MRR_df = pd.DataFrame(columns=["Project","Version","Method"]+data_cols)
topK_df = pd.DataFrame(columns=["Project","Version","Method"]+data_cols)
RFC_df = pd.DataFrame(columns=["Project","Version","Total","Covf", "RFC"])
Test_df = pd.DataFrame(columns=["Project","Version","TestSuite","TestCase"])
FileLine_df = pd.DataFrame(columns=["Project","Version","FileLine"])

for Version in range(1,18):
# for Version in range(1,2):
    data_path = r"./Results/gson_" + str(Version) + "_buggy"
    # read the buggy methods
    fp = open(os.path.join(data_path, "buggy_methods.txt"), mode='r')
    buggy_methods = fp.read()
    buggy_methods = buggy_methods.strip().split("\n")
    fp.close()

    # read the buggy lines
    fp = open(os.path.join(data_path, "buggy_lines.txt"), mode='r')
    buggy_lines = fp.read()
    buggy_lines = buggy_lines.strip().split("\n")
    fp.close()
    buggy_classes = [buggy_line.split("#")[0].split(".")[0].replace("/",".") for buggy_line in buggy_lines]

    # judge the buggy methods
    buggy_methods_judge = []
    for buggy_method in buggy_methods:
        judge_flag = False
        for buggy_class in buggy_classes:
            if buggy_class in buggy_method and judge4method(buggy_method, buggy_class):
                judge_flag = True
        if judge_flag:
            buggy_methods_judge.append(buggy_method)
    buggy_methods = buggy_methods_judge

    # read the Rank data
    # Rank_df = pd.read_csv(os.path.join(data_path,"MethodRank.csv"), header=0)
    Rank_df = pd.read_csv(os.path.join(data_path,"MethodRankRFC.csv"), header=0)

    # Calculate EXAM, MRR
    for buggy_method in buggy_methods:
        buggy_method_item = Rank_df[Rank_df["Method"]==buggy_method]
        if buggy_method_item.shape[0] == 1:
            # OK!
            buggy_index = buggy_method_item.index[0]

            EXAM_dict = {
                data_col: buggy_method_item.loc[buggy_index, data_col] / Rank_df.shape[0] for data_col in data_cols
            }
            EXAM_dict["Project"] = Project
            EXAM_dict["Version"] = Version
            EXAM_dict["Method"] = buggy_method
            EXAM_df = EXAM_df.append(EXAM_dict, ignore_index=True)

            MRR_dict = {
                data_col: 1 / buggy_method_item.loc[buggy_index, data_col] for data_col in data_cols
            }
            MRR_dict["Project"] = Project
            MRR_dict["Version"] = Version
            MRR_dict["Method"] = buggy_method
            MRR_df = MRR_df.append(MRR_dict, ignore_index=True)
            
            topK_dict = {
                data_col: buggy_method_item.loc[buggy_index, data_col] for data_col in data_cols
            }
            topK_dict["Project"] = Project
            topK_dict["Version"] = Version
            topK_dict["Method"] = buggy_method
            topK_df = topK_df.append(topK_dict, ignore_index=True)
    
    # Collect ALL, Covf, RFC
    fp = open(os.path.join(data_path, "all_methods.txt"), mode='r')
    all_methods = fp.read()
    all_methods = all_methods.strip().split("\n")
    fp.close()

    fp = open(os.path.join(data_path, "covf_methods.txt"), mode='r')
    covf_methods = fp.read()
    covf_methods = covf_methods.strip().split("\n")
    fp.close()

    fp = open(os.path.join(data_path, "RFC_methods.txt"), mode='r')
    RFC_methods = fp.read()
    RFC_methods = RFC_methods.strip().split("\n")
    fp.close()

    RFC_df = RFC_df.append({
        "Project": Project,
        "Version": Version,
        "Total": len(all_methods),
        "Covf": len(covf_methods),
        "RFC": len(RFC_methods)

    }, ignore_index=True)

    # Collect Test Data
    fp = open(os.path.join(data_path, "testsuites.txt"), mode='r')
    testsuites = fp.read()
    testsuites = len(testsuites.strip().split("\n"))
    fp.close()

    fp = open(os.path.join(data_path, "testcases.txt"), mode='r')
    testcases = fp.read()
    testcases = len(testcases.strip().split("\n"))
    fp.close()
    Test_df = Test_df.append({
        "Project": Project,
        "Version": Version,
        "TestSuite": testsuites,
        "TestCase": testcases

    }, ignore_index=True)

    # Collect File Line Count
    fp = open(os.path.join(data_path, "FileLineCount.txt"), mode='r')
    FileLineCount = fp.read()
    FileLineCount = int(FileLineCount.strip())
    fp.close()

    FileLine_df = FileLine_df.append({
        "Project": Project,
        "Version": Version,
        "FileLine": FileLineCount
    }, ignore_index=True)


EXAM_df.to_csv("./EXAM.csv", index=False)
MRR_df.to_csv("./MRR.csv", index=False)
topK_df.to_csv("./topK.csv", index=False)
RFC_df.to_csv("./RFC.csv", index=False)
Test_df.to_csv("./TestData.csv", index=False)
FileLine_df.to_csv("./FileLine.csv", index=False)


AverageMRR_Df = pd.DataFrame(columns=["Project"]+data_cols, index=[1])
AverageMRR_Df["Project"] = Project
AverageMRR_Df[data_cols] = MRR_df[data_cols].mean(axis=0)
AverageMRR_Df.to_csv("./AverageMRR.csv", index=False)

top_K_df = pd.DataFrame(columns=["Project", "topK"]+data_cols, index=[0,1,2])
topK = [1,3,5]
for i in top_K_df.index:
    top_K_df["Project"] = Project
    top_K_df["topK"] = topK
    for data_col in data_cols:
        top_K_df.loc[i, data_col] = topK_df[topK_df[data_col] <= topK[i]].shape[0]
top_K_df.to_csv("./top_K.csv",index=False)

RFC_overall_df = pd.DataFrame(columns=["Project","Statistic","Total","Covf", "RFC"], index=[0,1])
RFC_overall_df.loc[0, "Project"] = Project
RFC_overall_df.loc[0, "Statistic"] = "Sum"
RFC_overall_df.loc[0, ["Total","Covf", "RFC"]] = RFC_df[["Total","Covf", "RFC"]].sum()
RFC_overall_df.loc[1, "Project"] = Project
RFC_overall_df.loc[1, "Statistic"] = "Mean"
RFC_overall_df.loc[1, ["Total","Covf", "RFC"]] = RFC_df[["Total","Covf", "RFC"]].mean().astype(int)
RFC_overall_df.loc[2, "Project"] = Project
RFC_overall_df.loc[2, "Statistic"] = "Percentage"
RFC_overall_df.loc[2, ["Total","Covf", "RFC"]] = RFC_overall_df.loc[1, ["Total","Covf", "RFC"]] / RFC_overall_df.loc[1, "Total"]
RFC_overall_df.to_csv("./RFC_overall.csv",index=False)

VersionUsedCount = len(list(set(topK_df["Version"].to_list())))
fp = open("./VersionUsedCount.txt", mode='w')
fp.write(str(VersionUsedCount))
fp.close()