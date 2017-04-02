from sklearn import metrics
from sklearn.svm import SVC,LinearSVC
from sklearn.metrics import accuracy_score
from sklearn import datasets
import sklearn
import pandas
import numpy
import csv
from sklearn.multiclass import OneVsRestClassifier
# load data
df=datasets.load_()

#Storing the attribute names
attribute=[]
with open('SPECTF.csv', 'r') as f:
    first_line = f.readline()
attributes=first_line.split(',')
attributes=attributes[:-1]
print attributes
#Separating every record without the Class Label
X = df.data
print "X"
print X

#Separating only the Class Labels for all Records
Y = df.target
print "Y"
print Y
# fit a SVM model to the data
model = OneVsRestClassifier(LinearSVC(random_state=0))
model.fit(X, Y)
# print(model)
# make predictions


expected = Y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print (accuracy_score(expected, predicted))
