from sklearn import metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas
import numpy
import csv
import random
import copy


# Load csv file
def loaddata1(dataset1, dataset2):
	dataframetrain = pandas.read_csv(dataset1)
	# Separating every record without the Class Label
	trainX = dataframetrain.values[:, 0:dataframetrain.shape[1] - 1]
	# Separating only the Class Labels for all Records
	trainY = dataframetrain.values[:, dataframetrain.shape[1] - 1]
	dataframetest = pandas.read_csv(dataset2)
	# Separating every record without the Class Label
	testX = dataframetest.values[:, 0:dataframetest.shape[1] - 1]
	# Separating only the Class Labels for all Records
	testY = dataframetest.values[:, dataframetest.shape[1] - 1]
	# print	trainX,trainY,testX,testY
	return trainX, trainY, testX, testY


def classifyandpredict(trainX, trainY, testX, testY):
	model = SVC(kernel='poly')
	model.fit(trainX, trainY)
	expected = testY
	predicted = model.predict(testX)
	return predicted, expected


def crossvalidation(dataset, n_folds):
	with open(dataset, 'r') as file:
		reader = csv.reader(file)
		dataset = list(reader)
		dataset = dataset[1:]
		total = len(dataset)
		dataset_split = list()
		dataset_copy = copy.deepcopy(dataset)
		fold_size = int(len(dataset) / n_folds)
		for i in range(n_folds):
			fold = list()
			while len(fold) < fold_size:
				index = random.randrange(len(dataset_copy))
				fold.append(dataset_copy.pop(index))
			dataset_split.append(fold)

		for fold in dataset_split:
			train_set = list(dataset_split)
			train_set.remove(fold)
			train_set = sum(train_set, [])
			test_set = list()
			for row in fold:
				row_copy = list(row)
				test_set.append(row_copy)

			trainX, trainY = splitdatatarget(train_set)

			testX, testY = splitdatatarget(test_set)

			predicted, expected = classifyandpredict(trainX, trainY, testX, testY)
			return predicted, expected


def splitdatatarget(datalist):
	X = list()
	Y = list()
	for data in datalist:
		X.append(data[0:len(data) - 1])
		Y.extend(data[len(data) - 1:len(data)])
	return X, Y


def main():
	Averageaccuracy = 0
	metriclist = list()
	dataset = ["merged.csv", "merged1.csv"]
	for i in range(len(dataset)):
		for k in range(len(dataset)):
			if (i != k):
				trainX, trainY, testX, testY = loaddata1(dataset[i], dataset[k])
				predicted, expected = classifyandpredict(trainX, trainY, testX, testY)
				metriclist.append((copy.deepcopy(predicted), copy.deepcopy(expected)))
			else:
				predicted, expected = crossvalidation(dataset[i], 10)
				metriclist.append((copy.deepcopy(predicted), copy.deepcopy(expected)))
	print metriclist
	for mlist in metriclist:
		# summarize the fit of the model
		print(metrics.classification_report(mlist[1], mlist[0]))
		print(metrics.confusion_matrix(mlist[1], mlist[0]))
		Averageaccuracy += accuracy_score(mlist[1], mlist[0])
		print "Accuracy:", (accuracy_score(mlist[1], mlist[0])) * 100, "%"

	print "Average Accuracy :", (Averageaccuracy / len(metriclist)) * 100, "%"


main()
