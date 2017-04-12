'''
IMPORTANT
Instructions to run this program
To use this program as module calling load_and_run(filename,number_of_iterations,BenignClassValue)
returns a rank array'''
import pandas as pd
import numpy as np
import random
import math
import os


'''The relief algorithm'''
def relief(df, m, label):
    print "REl entered"
    f_weight = np.zeros(shape=df.shape[1]-1)
    df_wlabel = get_dataframe_with_label(df, label)
    df_wolabel = get_dataframe_without_label(df, label)
    for i in f_weight:
        i = 0
    time=0
    for featurenumber in range(df.shape[1]-1):
        for j in range(m):
            os.system('clear')
            time=time+1
            print ((1.0*time)/((df.shape[1]-1)*m))*100.0,"%"
            randomindex = random.randint(0, df.shape[0]-1)
            featurevector = df.iloc[randomindex, i]  # fixed feature random index
            f_weight[featurenumber] = f_weight[featurenumber] - (math.pow(featurevector - nearest(df_wlabel, featurevector, featurenumber), 2)
                                         + math.pow(featurevector - nearest(df_wolabel, featurevector, featurenumber),2))
        f_weight[featurenumber] = f_weight[featurenumber] / m
    print f_weight
    array = np.array(f_weight)
    temp = array.argsort()
    ranks = np.empty(len(array), int)
    ranks[temp] = np.arange(len(array))
    print ranks
    np.savetxt("ReliefRanks1.csv", ranks, delimiter=",")
    return ranks.tolist()

'''This function is used to the dataframe that contains a given class label'''
def get_dataframe_with_label(df, label):
    n_df = pd.DataFrame(columns=df.columns)
    row = 0
    for i in range(df.shape[0]):
        if (df.loc[i]['Class'] == label):
            n_df.loc[row] = df.loc[i]
            row = row + 1
    return n_df

'''This function is used to the dataframe that does not contain a given class label'''

def get_dataframe_without_label(df, label):
    n_df = pd.DataFrame(columns=df.columns)
    row = 0
    for i in range(df.shape[0]):
        if (df.loc[i]['Class'] != label):
            n_df.loc[row] = df.loc[i]
            row = row + 1
    return n_df

'''Used to find the nearest miss or nearest hit
nearest miss - Data Point whose feature vector is the closest to a chosen vector point and does NOT
belong to the same class label
nearest hit - Data Point whose feature vector is the closest to a chosen vector point and
belongs to the same class label'''

def nearest(df, featurevector, featurenumber):
    smallest = 0
    smallestvalue = df.iloc[0][featurenumber]
    for i in range(df.shape[0]):
        if abs(df.iloc[i][featurenumber] - featurevector) < smallestvalue:
            smallestvalue = df.iloc[i][featurenumber] - df.iloc[smallest][featurenumber]
            smallest = i
    return df.iloc[smallest][featurenumber]

'''Used to return relief score'''
def load_and_run(filename,m,BenignClassValue):
    return relief(pd.read_csv(filename),m,BenignClassValue)
def main():
    x=relief(pd.read_csv("fullfeaturedataset.csv"), 100, "None")
    return x

if __name__ == '__main__':
    main()
