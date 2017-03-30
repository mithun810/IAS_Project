import pandas as pd
import numpy as np
import csv
#csv will be feature name - rank 1 - rank 2 - rank 3

def loaddata(filename):
	dataframe = pd.read_csv(filename)
	return dataframe.values

def featureensemble(array,k,n):
	newranks=list()
	for i in range(203):
		sum1=0
		average=0
		for j in range(1,2):
			sum1+=array[i][j]
		average=sum1/2
		print average
		newranks.append(average)
	return newranks


#def selectbestk(k):


def main():
	array=loaddata("ranks.csv")
	print array
	k=20 #No of features to be selected
	n=203 #No of features in total 
	average=featureensemble(array,k,n)
	print average
if __name__ == '__main__':
	main()