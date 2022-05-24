#!usr/bin/python3

import os
from math import ceil, floor
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
random_seed = 1

sample_scale = 10

def my_round(f):
    if f-floor(f)>=0.5:
        return ceil(f)
    else:
        return floor(f) 

classes = os.listdir("./MAResults")

fp = open("../test_for_class/covfclasses.txt",mode='r')
covfclasses = fp.readlines()
fp.close()
covfclasses = [covfclass.strip() for covfclass in covfclasses]

mutants = [i for i in range(sample_scale)]

ClassDis = pd.DataFrame(columns=["Class"]+mutants)

for c in classes:
    if c in covfclasses:
        # print(c)
        if os.path.exists(os.path.join("./MAResults",c,"MutantDis.csv")):
            MutantDis_c = pd.read_csv(os.path.join("./MAResults",c,"MutantDis.csv"), header=0, index_col=0)
            # print(MutantDis_c.head())
            # print(MutantDis_c.shape[0])
            if MutantDis_c.shape[0] < sample_scale:
                MutantDis_c = MutantDis_c.sample(MutantDis_c.shape[0],random_state=random_seed,ignore_index=True)
            else:
                MutantDis_c = MutantDis_c.sample(sample_scale,random_state=random_seed,ignore_index=True)
            # print(MutantDis_c)
            ClassDisItem = {"Class":c}
            for i in MutantDis_c.index:
                ClassDisItem[i] = MutantDis_c.loc[i,"MutantDis"] 
            ClassDis = ClassDis.append(ClassDisItem, ignore_index=True)

InsensitiveClass = []
SensitiveClass = []
InvalidClass = []
for i in ClassDis.index:
    mds = ClassDis.loc[i, mutants].to_list()
    mds = [md for md in mds if not pd.isna(md)]
    if mds:
        md_dict = {}
        for md in mds:
            if md not in md_dict.keys():
                md_dict[md] = 1
            else:
                InsensitiveClass.append(i)
                break
    else:
        InvalidClass.append(i)

SensitiveClass = [i for i in ClassDis.index if i not in InsensitiveClass and i not in InvalidClass]
# ClassDis["ClassDis"] = ClassDis.loc[Insensitive, mutants].mode(axis=1).mean(axis=1)
ClassDis["ClassDis"] = ClassDis[mutants].mean(axis=1)
ClassDis.loc[InsensitiveClass+SensitiveClass ,"ClassDis"]=ClassDis.loc[InsensitiveClass+SensitiveClass ,"ClassDis"].map(my_round).astype(int)
# ClassDis["ClassDis"] = ClassDis[mutants].mean(axis=1).map(my_round)
# ClassDis["ClassDis"] = ClassDis["ClassDis"].astype(int)

if len(InsensitiveClass) == 1:
    cd_mean=ClassDis.loc[InsensitiveClass, "ClassDis"].mean()
    cd_std=0
    InsensitiveClassRFC = InsensitiveClass
else:
    InsensitiveClassRFC = []
    cd_mean = ClassDis.loc[InsensitiveClass, "ClassDis"].mean()
    cd_std = ClassDis.loc[InsensitiveClass, "ClassDis"].std()
    for i in InsensitiveClass:
        if cd_mean-3*cd_std < ClassDis.loc[i, "ClassDis"] < cd_mean+3*cd_std:
            InsensitiveClassRFC.append(i)

ClassDis = ClassDis.sort_values(by="Class")
# print(ClassDis)
# print([cd_mean-3*cd_std, cd_mean+3*cd_std])

RFC_classes = ClassDis.loc[InsensitiveClassRFC+SensitiveClass+InvalidClass,"Class"].to_list()

ClassDis.to_csv("./ClassDis.csv",index=False)

fp = open("./RFC_classes.txt",mode="w")
fp.write("\n".join(RFC_classes))
fp.close()