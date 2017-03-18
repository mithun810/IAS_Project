import pandas as pd
import numpy as np
import random
import math
def relief(df,m,label):
    f_weight=np.zeros(shape=df.shape[0])
    df_wlabel=get_dataframe_with_label(df,label)
    df_wolabel=get_dataframe_without_label(df,label)
    
    for i in f_weight:
        i=0
    for i in range(df.shape[1]):
        for j in range(m):
            randomindex=random.randint(0,df.shape[0])
            f=df.iloc[randomindex,i]
            f_weight[i]=f_weight[i]-(math.pow((f-nearest(df_wlabel,f,i)),2)+math.pow(f-nearest(df_wolabel,f,i)))
        f_weight[i]=f_weight[i]/m

    return f_weight

def get_dataframe_with_label(df,label):
    n_df=pd.DataFrame(columns=df.columns)
    row=0
    for i in range(df.shape[0]):
        if(df.loc[i]['ClassLabel']==label):
            a.loc[row]=df.loc[i]
            row=row+1
    return n_df

def get_dataframe_without_label(df,label):
    n_df=pd.DataFrame(columns=df.columns)
    row=0

    for i in range(df.shape[0]):
        if(df.loc[i]['ClassLabel']!=label):
            n_df.loc[row]=df.loc[i]
            row=row+1
    return n_df
def nearest(df,x,feature):
    smallest=0
    for i in range(df.shape[0]):
        if(df.iloc[i,x]<df.iloc[smallest,x]):
            smallest = i
    return df.iloc[smallest,x]
