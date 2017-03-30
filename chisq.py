import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
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
# Feature extraction
test = SelectKBest(score_func=chi2, k=20)
fit = test.fit(X, Y)
# summarize scores
#numpy.set_printoptions()
print "Chi Square Scores for all Features"
fit.scores_ = [0 if x != x else x for x in fit.scores_]
print(fit.scores_)
#Storing a copy of the scores
Chiscores=fit.scores_
selectedattributes=[]
#Calculating ranks and writing in csv file
print "Ranks"
array = numpy.array(Chiscores)
#temp = array.argsort()
n=len(array)
temp=array.argsort()[::-1][:n]
ranks = numpy.empty(len(array), int)
ranks[temp] = numpy.arange(len(array))
list_of_cols=[attributes,ranks]
w = csv.writer(open("ranks.csv","w"))
w.writerows(zip(*list_of_cols))
print ranks
#Selecting top best 20 features based on Chi Squares
for i in range(20):
	maxvalue=max(fit.scores_)
	print maxvalue
	indexattribute=numpy.argmax(fit.scores_,axis=None,out=None)
	selectedattributes.append(attributes[indexattribute])
	fit.scores_=numpy.delete(fit.scores_,indexattribute)
	attributes.pop(indexattribute)
print selectedattributes






