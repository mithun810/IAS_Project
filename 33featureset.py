import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import Chisq
import Gainratio
import Relief
import csv
import copy


# For unified

def load_csv(filename, ranks):
    dataframe = pandas.read_csv(filename)
    with open(filename, 'r') as f:
        first_line = f.readline()
    attributes = first_line.split(',')
    attributes = attributes[:-1]
    return generatefeatureset(attributes, dataframe, ranks)


def getRanksavg():
    filenames = ['merged.csv', 'merged1.csv']
    ranks = list()
    for filename in filenames:
        ranks.append(getRanks(filename))
    avgRanks = list()
    for index in range(len(ranks[0])):
        temp=list()
        for rank in ranks:
            temp.append(rank[index])
        avgRanks.append(ensemble(temp))


def getRanks(filename):
    Ranks = list()
    df = pandas.read_csv("ReliefRanks2.csv", header=None)
    print "Chi Square"
    Ranks.append(Chisq.load_csv(filename).tolist())
    print "Gain Ratio"
    Ranks.append((Gainratio.load_csv(filename)).tolist())
    print "Relief"
    Ranks.append(list(zip(*(df.values.tolist()))[0]))
    return Ranks


def ensemble(ranks):
    ens = list()
    for index in range(len(ranks[0])):
        temp = 0
        for rank in ranks:
            print index
            temp = temp + rank[index]
        temp = temp / len(ranks)
        ens.append(temp)
    return ens


def generatefeatureset(attributes, dataset, ranks):
    attributesre = list()
    k = [5, 10, 20, 30]
    featureset = list()
    for index, rank in enumerate(ranks):
        for j in range(len(k)):
            Selectedattributes = list()
            newdata = list()
            attributesre = copy.deepcopy((attributes))
            Ranks = copy.deepcopy(rank)
            R = copy.deepcopy(Ranks)
            for l in range(k[j]):
                # print Ranks
                indexminvalue = R.index(min(R))
                Selectedattributes.append(attributesre[indexminvalue])
                newdata.append(dataset.iloc[:, indexminvalue].values.tolist())
                del R[indexminvalue]
                del attributesre[indexminvalue]
            Selectedattributes = ["uni_FS" + str(index) + "_Top_" + str(k[j])] + Selectedattributes
            featureset.append(Selectedattributes)
        # featuresetcol.append("uni_FS"+str(index)+"_Top_"+str(k[j]))
        # Generating new dataset based on Selected Features
        # final_df = pandas.DataFrame.from_records(zip(*newdata), columns=Selectedattributes)
        # final_df.to_csv("uni_FS"+str(index)+"_Top_"+str(k[j])+'featureset'+'.csv',index=None)
    return featureset


def main():
    filename = 'unified.csv'
    ranks = getRanks(filename)
    ens = ensemble(ranks)
    # print ens
    ranks.append(ens)
    print ranks
    featureset = load_csv(filename, ranks)
    w = csv.writer(open("33FeatureSet.csv", "w"))
    w.writerows(featureset)


main()
