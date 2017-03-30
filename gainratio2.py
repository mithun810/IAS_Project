from sklearn.tree import DecisionTreeClassifier
import pandas
import numpy
import csv
# load data
dataframe = pandas.read_csv("merged.csv")
print len(dataframe)
print len(dataframe.columns)
array = dataframe.values
#Storing the attribute names
attribute=[]
with open('merged.csv', 'r') as f:
    first_line = f.readline()
attributes=first_line.split(',')
attributes=attributes[:-1]
print attributes
#Separating every record without the Class Label
X = array[:,0:204]
print "X"
print X
#Separating only the Class Labels for all Records
Y = array[:,204]
print "Y"
print Y
clf = DecisionTreeClassifier(criterion='entropy')
fit = clf.fit(X, Y)

importances = fit.feature_importances_
array = numpy.array(importances)
#temp = array.argsort()
n=len(array)
temp=array.argsort()[::-1][:n]
ranks = numpy.empty(len(array), int)
ranks[temp] = numpy.arange(len(array))
list_of_cols=[attributes,ranks]
print ranks
