import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load data
dataframe = pandas.read_csv("IRIS.csv")
print dataframe
array = dataframe.values
#Storing the attribute names
attribute=[]
with open('IRIS.csv', 'r') as f:
    first_line = f.readline()
attributes=first_line.split(',')
attributes=attributes[:-1]
print attributes
#Separating every record without the Class Label
X = array[:,0:4]
print X
#Separating only the Class Labels for all Records
Y = array[:,4]
print Y
# Feature extraction
test = SelectKBest(score_func=chi2, k=2)
fit = test.fit(X, Y)
# summarize scores
numpy.set_printoptions(precision=3)
print "Chi Square Scores for all Features"
print(fit.scores_)
selectedattributes=[]
for i in range(2):
	maxvalue=max(fit.scores_)
	print maxvalue
	indexattribute=numpy.argmax(fit.scores_,axis=None,out=None)
	selectedattributes.append(attributes[indexattribute])
	fit.scores_=numpy.delete(fit.scores_,indexattribute)
	attributes.pop(indexattribute)
print selectedattributes