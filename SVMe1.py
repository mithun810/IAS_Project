                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                from sklearn import metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas
import numpy
import csv
# load data
def load_data(filename):
    dataframe = pandas.read_csv(filename)
    print len(dataframe)
    print len(dataframe.columns)
    array = dataframe.values
    return dataframe,array

#Storing the attribute names
# attribute=[]
# with open('Newdata.csv', 'r') as f:
#     first_line = f.readline()
# attributes=first_line.split(',')
# attributes=attributes[:-1]
# print attributes
#Separating every record without the Class Label
def getData(dataframe,array):
    X = array[:,0:dataframe.shape[1]-1]
    print "X"
    return X

#Separating only the Class Labels for all Records
def getTarget(dataframe,array):
    Y = array[:,dataframe.shape[1]-1]
    print "Y"
    return Y
def classifyandpredict(X,Y):
# fit a SVM model to the data
    model = SVC()
    model.fit(X, Y)
    # print(model)
    # make predictions
    expected = Y
    predicted = model.predict(X)
    return predicted,expected

def main():
    dataframe,array = load_data("Newdata.csv")
    X = getData(dataframe,array)
    Y = getTarget(dataframe,array)
    predicted, expected = classifyandpredict(X,Y)
    # summarize the fit of the model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    print "Accuracy : ",(accuracy_score(expected, predicted))*100,"%"
if __name__ == '__main__':
    main()
