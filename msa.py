print(__doc__)
import os
from spoa import poa

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import Levenshtein
import csv
import pandas as pd

%matplotlib inline
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

# Distance metric
def lev_metric(x, y):
    i, j = int(x[0]), int(y[0])
    return (Levenshtein.distance(b1[i], b1[j]))

df = pd.read_csv("~/Desktop/align/knx.csv")
b1 = df.Protocols.to_list()

X1 = np.arange(len(b1)).reshape(-1, 1) 

# Defining DBSCAN Parameters and clustering
db = DBSCAN(eps = 2, min_samples = 2, metric = lev_metric)
predictions = db.fit_predict(X1)

ss = StandardScaler()
X = ss.fit_transform(X1)
db = DBSCAN(eps = 2, min_samples = 2, metric = lev_metric)
db.fit(X)
y_pred = db.fit_predict(X)
plt.scatter(X[:,0], X[:,],c=y_pred, cmap='Paired')
plt.title("DBSCAN")

# Printing results 
tmp = pd.DataFrame({'messages': b1, 'cluster_id': predictions})
tmp.sort_values(by = ['cluster_id'], ascending = True, inplace = True)
print (tmp)

df_group = (tmp.groupby(['cluster_id'])['messages'].apply(','.join).reset_index())

for i,item in df_group.iterrows():
    x = df_group.loc[i]['messages'].split(",")
    consensus, msa = poa(x)
    print(consensus)