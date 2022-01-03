import pandas as pd 
import numpy as np 
lc = pd.read_excel('MathAns-1.xls',sheet_name='math1')
data = lc.head()
print(format(data))