import os
import javalang
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

FileLineCount_df = pd.DataFrame(columns=["File Name", "Line Count"])
# SrcPath = "../../src/main/java/org/apache/commons/compress"
SrcPath = "../../gson/src/main/java/com/google/gson"
for dirpath, dirnames, filenames in os.walk(SrcPath):
    for filename in filenames:
        if filename.split('.')[-1] == "java":
            FileName = os.path.join(dirpath, filename)

            fp = open(FileName, "r")
            src = fp.read()
            fp.close()
            tokens = javalang.tokenizer.tokenize(src)
            LineCount=0
            for each_t in tokens:
                LineCount = each_t.position[0]
            
            FileLineCount_df = FileLineCount_df.append({
                "File Name": FileName, 
                "Line Count": LineCount
            }, ignore_index=True)
FileLineCount_df.to_csv("FileLineCount.csv",index=False)
FileLineCount = FileLineCount_df["Line Count"].sum()
fp = open("./FileLineCount.txt", mode='w')
fp.write(str(FileLineCount))
fp.close()

