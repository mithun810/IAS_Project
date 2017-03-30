import numpy as np
import matplotlib.pyplot as plt
import pandas
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
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
# Build a classification task using 3 informative features


# Build a forest and compute the feature importances
forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

forest.fit(X, Y)
importances = forest.feature_importances_
print sorted(importances,reverse=True)
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()