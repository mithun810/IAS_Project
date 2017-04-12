from sklearn.tree import DecisionTreeClassifier
import pandas
import numpy
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
	#print "X"
	#print X
	#Separating only the Class Labels for all Records
	Y = array[:,dataframe.shape[1]-1]
	#print "Y"
	#print Y
	return featureextraction(X,Y,attributes)



# Feature extraction
def featureextraction(X,Y,attributes):
	print "Gain features entered"
	clf = DecisionTreeClassifier(criterion='entropy')
	fit = clf.fit(X, Y)
	# summarize scores
	importances = fit.feature_importances_
	#Function to assign ranks to all Features
	return assignranks(importances,attributes)

def assignranks(importances,attributes):
	#Storing a copy of the scores
	print "Gain ranks entered"
	Gainratioscores =importances
	#Calculating ranks and writing in csv file
	array = numpy.array(Gainratioscores)
	n=len(array)
	temp=array.argsort()[::-1][:n]
	ranks = numpy.empty(len(array), int)
	ranks[temp] = numpy.arange(len(array))
	return ranks

def writetofile(ranks,attributes):
	list_of_cols=[ranks]
	w = csv.writer(open("someranksgain.csv","w"))
	w.writerows(zip(*list_of_cols))
	print "Gain file created"
	return

def selectbestfeatures(fitscores,attributes,k):
	#Selecting top best 20 features based on Chi Squares
	selectedattributes=[]
	for i in range(k):
		maxvalue=max(fitscores)
		indexattribute=numpy.argmax(fitscores,axis=None,out=None)
		selectedattributes.append(attributes[indexattribute])
		fitscores=numpy.delete(fitscores,indexattribute)
		attributes.pop(indexattribute)

def main():
	filename="fullfeaturedataset.csv"
	X,Y,attributes=load_csv(filename)
	ranks,attributes,importances=featureextraction(X,Y,attributes)
	writetofile(ranks,attributes)
	#selectbestfeatures(importances,attributes,20)




