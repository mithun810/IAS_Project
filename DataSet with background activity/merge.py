import os
import pandas as pd
import numpy as np
import copy
mergelist=list()
for filename in os.listdir(os.getcwd()):
    if filename.endswith('csv') or filename == "merged.csv":
        df=pd.read_csv(filename)
        df['Class']=filename[0:len(filename)-4]
        mergelist.append(copy.deepcopy(df))
merge_df=pd.concat(mergelist)
merge_df.to_csv("merged.csv",columns=None)
