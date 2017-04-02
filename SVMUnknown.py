from sklearn import metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas
import numpy
import csv
import copy
import random
import pandas as pd
from sklearn import datasets
# load data
def load_data(filename):
    dataframe = pandas.read_csv(filename)
    #print len(dataframe)
    #print len(dataframe.columns)
    array = dataframe.values
    return dataframe,array


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

def getData(dataframe,array):
    X = array[:,0:dataframe.shape[1]-1]
    #print "X"
    return X

#Separating only the Class Labels for all Records ran
def getTarget(dataframe,array):
    Y = array[:,dataframe.shape[1]-1]
    #print "Y"
    return Y
def classifyandpredict(train_X,train_Y,test_X,test_Y):
# fit a SVM model to the data
    model = SVC()
    model.fit(train_X,train_Y)
    expected = test_Y
    predicted = model.predict(test_X)
    return predicted,expected

def main():
    dataframe,array = load_data("Newdata.csv")
    X = getData(dataframe,array)
    Y = getTarget(dataframe,array)
    Xn, Yn = get_dataframe_with_label(X, Y, 'None')
    Xo, Yo = get_dataframe_without_label(X, Y, 'None')
    train_X = copy.deepcopy(Xo)
    train_Y = copy.deepcopy(Yo)
    test_X = list()
    test_Y = list()
    Xn_train_temp = copy.deepcopy(Xn)
    Yn_train_temp = copy.deepcopy(Yn)
    Xn_test_temp = list()
    Yn_test_temp = list()
    dataframe1, array1 = load_data("YankerSelected.csv")
    Xunknown = getData(dataframe1, array1)
    Yunknown = getTarget(dataframe1, array1)
    # df=datasets.load_iris()
    # X=df.data
    # Y=df.target
    # predicted, expected = classifyandpredict(X,Y)
    #predicted, expected = classifyandpredict(X,Y)


    for j in range(len(Yunknown)):
        randomindex = random.randrange(0, len(Xn_train_temp))
        Xn_test_temp.append(Xn_train_temp[randomindex])
        Yn_test_temp.append(Yn_train_temp[randomindex])
        del Xn_train_temp[randomindex]
        del Yn_train_temp[randomindex]
    train_X.extend(Xn_train_temp)
    train_Y.extend(Yn_train_temp)
    test_X.extend(Xn_test_temp)
    test_Y.extend(Yn_test_temp)
    test_X.extend(Xunknown)
    test_Y.extend(Yunknown)

    for idx, X in enumerate(train_Y):
        if X != 'None':
            train_Y[idx] = 'Worm'
    for idx, X in enumerate(test_Y):
        if X != 'None':
            test_Y[idx] = 'Worm'

    predicted, expected = classifyandpredict(train_X,train_Y,test_X,test_Y )


    print(metrics.classification_report(predicted, expected))
    print(metrics.confusion_matrix(predicted, expected))
    print "Accuracy : ",(accuracy_score(predicted, expected))*100,"%"







if __name__ == '__main__':
    main()
