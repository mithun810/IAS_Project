#!/usr/bin/python
import pandas as pd
import numpy as np
import sys
df = pd.read_csv(sys.argv[1],low_memory=False)
for i in reversed(xrange(df.shape[0])):
    if(i%6!=0):
        df=df.drop(i)

df.to_csv(sys.argv[1][0:int(len(sys.argv[1])-4)]+'_shrunk.csi',index=False)
print df

