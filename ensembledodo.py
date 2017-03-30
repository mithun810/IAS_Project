import pandas as pd
import numpy as np

FULL_DATASET = 'merged.csv'
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
	full_df=pd.read_csv(FULL_DATASET)

	return selectkbest(full_df,df,score,150)

def selectkbest(full_df,df,scores,k):
	newdata=list()
	attributes=df.icol(0)
	Selectedattributes=list()
	for i in range(k):
		minvalue=min(scores)
		indexminvalue=np.argmin(scores,axis=None,out=None)
		Selectedattributes.append(attributes[indexminvalue])
		print attributes[indexminvalue]
		newdata.append(full_df[attributes[indexminvalue]])
		scores=np.delete(scores,indexminvalue)
	print Selectedattributes
	final_df = pd.DataFrame.from_records(zip(*newdata), columns=Selectedattributes)
	final_df['Class']=full_df.icol(-1)
	final_df.to_csv("Newdata.csv")
	#print newdata

def writetofile(newdata):
	pass

def main():
	print ensemble('ranks.csv')
if __name__ == '__main__':
	main()