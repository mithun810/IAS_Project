import pandas as pd
import numpy as np
def ensemble(filename):
	df=pd.read_csv(filename,header=None)
	score = np.zeros(shape=df.shape[0])

	for i in range(df.shape[0]):
		for j in range(df.shape[1]):
			if j==0:
				continue;
			else:
				score[i]=score[i]+df.iloc[i][j]
		score[i]=score[i]/(df.shape[1]-1);
	np.savetxt("AvgRanks.csv", score, delimiter=",")
	return selectkbest(df,score,20)

def selectkbest(df,scores,k):
	newdata=list()
	attributes=df.icol(0)
	Selectedattributes=list()
	for i in range(k):
		minvalue=min(scores)
		indexminvalue=np.argmin(scores,axis=None,out=None)
		Selectedattributes.append(attributes[indexminvalue])
		print attributes[indexminvalue]
		newdata.append(df[attributes[indexminvalue]].as_matrix)
		scores=np.delete(scores,indexminvalue)
	print Selectedattributes
	print newdata



def main():
	print ensemble('ranks.csv')
if __name__ == '__main__':
	main()