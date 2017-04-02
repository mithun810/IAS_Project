import pandas as pd
import numpy as np


#Read two files to get feature ranks (1) and the Original dataset (2)
def load_csv(filename1,filename2):
	df=pd.read_csv(filename1,header=None)
	print df
	score = np.zeros(shape=df.shape[0])
	full_df=pd.read_csv(filename2)
	print full_df

	return df,full_df,score


#Calculate Average Rank of each Feature and write it into a File
def ensemble(df,full_df,score):
	for i in range(df.shape[0]):
		for j in range(df.shape[1]):
			if j==0:
				continue;
			else:
				score[i]=score[i]+df.iloc[i][j]
		score[i]=score[i]/(df.shape[1]-1);
	np.savetxt("AvgRanks.csv", score, delimiter=",")
	return score

#Select best K features based on average ranks and generate new dataset based on selected features
def selectkbest(full_df,df,scores,k):
	newdata=list()
	attributes=df.icol(0)
	Selectedattributes=list()
	for i in range(k):
		minvalue=min(scores)
		indexminvalue=np.argmin(scores,axis=None,out=None)
		Selectedattributes.append(attributes[indexminvalue])
		newdata.append(full_df[attributes[indexminvalue]])
		scores=np.delete(scores,indexminvalue)
	print Selectedattributes
	#Generating new dataset based on Selected Features
	final_df = pd.DataFrame.from_records(zip(*newdata), columns=Selectedattributes)
	final_df['Class']=full_df.icol(-1)
	final_df.to_csv("YankerSelected.csv")
	

def writetofile(newdata):
	pass

def main():
	k=20
	df,full_df,score = load_csv('Ranksnew.csv','Yanker.csv')
	score = ensemble(df,full_df,score)
	print selectkbest(full_df,df,score,k)
if __name__ == '__main__':
	main()