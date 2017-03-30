from sklearn import metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas
import numpy
import csv
# load data
dataframe = pandas.read_csv("Newdata.csv")
print len(dataframe)
print len(dataframe.columns)
array = dataframe.values
#Storing the attribute names
attribute=[]
with open('Newdata.csv', 'r') as f:
    first_line = f.readline()
attributes=first_line.split(',')
attributes=attributes[:-1]
print attributes
#Separating every record without the Class Label
X = array[:,0:dataframe.shape[1]-1]
print "X"
print X
#Separating only the Class Labels for all Records
Y = array[:,dataframe.shape[1]-1]
print "Y"
print Y
# fit a SVM model to the data
model = SVC()
model.fit(X, Y)
print(model)
# make predictions
expected = Y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print (accuracy_score(expected, predicted))