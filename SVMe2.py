from sklearn import metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas
import numpy
import csv
import copy
import random
import pandas as pd
import math
from sklearn import datasets
# load data
def load_data(filename,features ):
    dataframe = pandas.read_csv(filename)
    print features
    df=dataframe[features]
    #print len(dataframe)
    #print len(dataframe.columns)
    array = df.values
    return df,array


#Separating every record without the Class Label

'''This function is used to the dataframe that contains a given class label'''
def get_dataframe_with_label(X, Y,label):
    Xwl=list()
    Ywl=list()
    for i in range(len(Y)):
        if label == Y[i]:
            Xwl.append(X[i])
            Ywl.append(Y[i])

    return Xwl,Ywl

'''This function is used to the dataframe that does not contain a given class label'''

def get_dataframe_without_label(X, Y,label):
    Xwl=list()
    Ywl=list()
    for i in range(len(Y)):
        if label != Y[i]:
            Xwl.append(X[i])
            Ywl.append(Y[i])

    return Xwl,Ywl

'''Get dataframe without class label'''
def getData(dataframe,array):
    X = array[:,0:dataframe.shape[1]-1]
    #print "X"
    return X

'''Get dataframe with only class label'''
#Separating only the Class Labels for all Records ran
def getTarget(dataframe,array):
    Y = array[:,dataframe.shape[1]-1]
    #print "Y"
    return Y

'''SVM using sklearn'''
def classifyandpredict(train_X,train_Y,test_X,test_Y):
# fit a SVM model to the data
    model = SVC(kernel='rbf',gamma=0.00002, C=10)
    model.fit(train_X,train_Y)
    expected = test_Y
    predicted = model.predict(test_X)
    return predicted,expected

def main():
    with open('33FeatureSet.csv', 'rb') as f:
        reader = csv.reader(f)
        featuresets = list(reader)
    feat=featuresets[1]
    features = list()
    for i in feat[1:]:
        if i != '':
            features.append(i)
        else:
            break
    features.append('Class')
    dataframe,array = load_data("unified.csv",features)
    X = getData(dataframe,array)
    Y = getTarget(dataframe,array)
    # df=datasets.load_iris()
    # X=df.data
    # Y=df.target
    # predicted, expected = classifyandpredict(X,Y)
    #predicted, expected = classifyandpredict(X,Y)
    Xn,Yn= get_dataframe_with_label(X,Y,'None')
    Xo,Yo = get_dataframe_without_label(X,Y,'None')
    classes = list()

    for i in Yo:
        if i not in classes:
            classes.append(i)
    itertr=2
    train_X=copy.deepcopy(Xo)
    train_Y=copy.deepcopy(Yo)
    test_X=list()
    test_Y=list()
    metriclist=list()
    '''Different combinations of testing and training'''
    for itertr1 in range(5):
        if itertr1==4:
            continue
        #print len(classes)
        randindex=random.randrange(0,len(classes))
        randlabel=classes[randindex]
        del classes[randindex]
        # temp_X=copy.deepcopy(train_X)
        # temp_Y=copy.deepcopy(train_Y)
        temp_X,temp_Y=get_dataframe_without_label(train_X,train_Y,randlabel)
        train_X=copy.deepcopy(temp_X)
        train_Y=copy.deepcopy(temp_Y)
        temp_X,temp_Y=get_dataframe_with_label(Xo,Yo,randlabel)
        test_X.extend(temp_X[0:len(temp_Y)/2])
        test_Y.extend(temp_Y[0:len(temp_Y)/2])
        dataadd=list()
        Xn_train_temp=copy.deepcopy(Xn)
        Yn_train_temp=copy.deepcopy(Yn)
        Xn_test_temp=list()
        Yn_test_temp=list()
        if itertr1==0:
            for j in range(len(Xn)/2):
                randomindex=random.randrange(0,len(Xn_train_temp))
                Xn_test_temp.append(Xn_train_temp[randomindex])
                Yn_test_temp.append(Yn_train_temp[randomindex])
                del Xn_train_temp[randomindex]
                del Yn_train_temp[randomindex]
        train_X.extend(Xn_train_temp)
        train_Y.extend(Yn_train_temp)
        test_X.extend(Xn_test_temp)
        test_Y.extend(Yn_test_temp)
        df = pd.DataFrame.from_records(train_X)
        copyof_train_Y=copy.deepcopy(train_Y)
        copyof_test_Y=copy.deepcopy(test_Y)
        wormcount=0
        for idx,X in enumerate(copyof_train_Y):
            if X!='None':
                copyof_train_Y[idx]='Worm'
        for idx,X in enumerate(copyof_test_Y):
            if X!='None':
                wormcount=wormcount+1
                copyof_test_Y[idx]='Worm'
        copyof_test_X=copy.deepcopy(test_X)
        copyof_test_Xn,copyof_test_Yn=get_dataframe_with_label(copyof_test_X,copyof_test_Y,'None')
        copyof_test_X,copyof_test_Y=get_dataframe_without_label(copyof_test_X,copyof_test_Y,'None')
        for iter in reversed(xrange(len(copyof_test_Y))):
            if iter==0:
                continue
            length = len(copyof_test_X)
            nlength = len(copyof_test_X) - wormcount
            div = math.ceil(length * 1.0 / len(copyof_test_Xn))
            if div==1.0:
                break
            length=len(copyof_test_X)
            nlength=len(copyof_test_X)-wormcount
            div=math.ceil(length*1.0/len(copyof_test_Xn))
            if (iter % div != 0):
                del copyof_test_Y[iter]
                del copyof_test_X[iter]
        copyof_test_X.extend(copyof_test_Xn)
        copyof_test_Y.extend(copyof_test_Yn)
        predicted, expected = classifyandpredict(train_X,copyof_train_Y,copyof_test_X,copyof_test_Y )
        metriclist.append((copy.deepcopy(predicted),copy.deepcopy(expected)))
    averageaccuracy=0
    for mlist in metriclist:
        print(metrics.confusion_matrix(mlist[1], mlist[0]))
        averageaccuracy=averageaccuracy+(accuracy_score(mlist[1], mlist[0]))
        print "Accuracy : ",(accuracy_score(mlist[1], mlist[0]))*100,"%"

    print "Average Accuracy : ", (averageaccuracy/len(metriclist)) * 100, "%"

    '''
        templist=list()
        for i in train_Y:
            if i not in templist:
                templist.append(i)
        print "Train",templist
        templist=list()
        for i in test_Y:
            if i not in templist:
                templist.append(i)
        print "Test",templist
        '''



    # summarize the fit of the model
    #print(metrics.classification_report(expected, predicted))
    #print(metrics.confusion_matrix(expected, predicted))
    #print "Accuracy : ",(accuracy_score(expected, predicted))*100,"%"
if __name__ == '__main__':
    main()
