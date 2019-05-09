import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
from sklearn import preprocessing
import matplotlib.pyplot as plt

dataset = pd.read_csv('test.csv')
#dataset.drop(dataset.index[98])
dataset = dataset.fillna('0')


# cluster rows
X = dataset.iloc[:, 1:].values
X_scaled = preprocessing.scale(X)

# find cutoff from dendrogram
'''
dendrogram = sch.dendrogram(sch.linkage(X_scaled, method = 'ward'))
plt.show()
'''

# hierarchical clustering
dist = sch.distance.pdist(X_scaled)
link = sch.linkage(dist, method='ward')
ind = sch.fcluster(link, 7.215, 'distance') #7.215 is cutoff observed from dendogram

# sort
clustered_row = dataset.assign(cluster = pd.Series(ind).values)
clustered_row = clustered_row.sort_values(['cluster','Grand Total'], ascending=[True,False])

# export
clustered_row.to_csv('clustered_row.csv')


# cluster columns
transpose = clustered_row.T
A = transpose.iloc[1:-2, :-1].values
A_scaled = preprocessing.scale(A)

#find cutoff from the dendorgram
'''
dendrogram = sch.dendrogram(sch.linkage(A_scaled, method = 'complete'))
plt.show()
'''

# hierarchical clustering
dist = sch.distance.pdist(A_scaled)
link = sch.linkage(dist, method='complete')
ind = sch.fcluster(link, 12.75, 'distance')

# sort
ind = np.concatenate([[0],ind,[ind.max()+1],[ind.max()+2]])
transpose = transpose.assign(cluster = pd.Series(ind).values)
transpose = transpose.sort_values(['cluster'], ascending=[True])
clustered_row_column = transpose.T

# export
clustered_row_column.to_csv('clustered_row_column.csv')
