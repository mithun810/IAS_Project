import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import csv

def load_csv(filename):
	dataframe = pandas.read_csv(filename)
	array = dataframe.values
	#Storing the attribute names
	with open(filename, 'r') as f:
		first_line = f.readline()
	attributes=first_line.split(',')
	attributes=attributes[:-1]
	#Separating every record without the Class Label
	X = array[:,0:dataframe.shape[1]-1]
	print "X"
	print X
	#Separating only the Class Labels for all Records
	Y = array[:,dataframe.shape[1]-1]
	print "Y"
	print Y
	return featureextraction(X,Y,attributes)

# Feature extraction
def featureextraction(X,Y,attributes):
	test = SelectKBest(score_func=chi2, k=20)
	fit = test.fit(X, Y)
	# summarize scores
	print "Chi Square Scores for all Features"
	fit.scores_ = [0 if x != x else x for x in fit.scores_]
	print(fit.scores_)
	#Function to assign ranks to all Features
	assignranks(fit.scores_,attributes)
	return fit.scores_


def assignranks(fitscores,attributes):
	#Storing a copy of the scores
	Chiscores=fitscores
	#Calculating ranks and writing in csv file
	print "Ranks"
	array = numpy.array(Chiscores)
	n=len(array)
	temp=array.argsort()[::-1][:n]
	ranks = numpy.empty(len(array), int)
	ranks[temp] = numpy.arange(len(array))
	list_of_cols=[attributes,ranks]
	w = csv.writer(open("ranks6.csv","w"))
	w.writerows(zip(*list_of_cols))
	#Funtion for getting best K features
	selectbestfeatures(fitscores,attributes,20)
	return

def selectbestfeatures(fitscores,attributes,k):
	#Selecting top best 20 features based on Chi Squares
	selectedattributes=[]
	for i in range(k):
		maxvalue=max(fitscores)
		print maxvalue
		indexattribute=numpy.argmax(fitscores,axis=None,out=None)
		selectedattributes.append(attributes[indexattribute])
		fitscores=numpy.delete(fitscores,indexattribute)
		attributes.pop(indexattribute)
	print "The Selected attributes are"
	print selectedattributes

def main():
	filename="fullfeaturedataset.csv"
	load_csv(filename)

main()




