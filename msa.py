import sys
import Levenshtein
from query.query import * 
from spoa import poa

import numpy as np
from sklearn.cluster import DBSCAN
import csv
import pandas as pd

# Distance metric
def lev_metric(x, y):
    i, j = int(x[0]), int(y[0])
    return (Levenshtein.distance(b1[i], b1[j]))

df = pd.read_csv("data//knx.csv")
b1 = df.Protocols.to_list()

X1 = np.arange(len(b1)).reshape(-1, 1) 

# Defining DBSCAN Parameters and clustering
db = DBSCAN(eps = 2, min_samples = 2, metric = lev_metric)
predictions = db.fit_predict(X1)


# Printing results 
tmp = pd.DataFrame({'messages': b1, 'cluster_id': predictions})
tmp.sort_values(by = ['cluster_id'], ascending = True, inplace = True)


df_group = (tmp.groupby(['cluster_id'])['messages'].apply(','.join).reset_index())

#print(df_group)

db = QUERY()

for i,item in df_group.iterrows():
    x = df_group.loc[i]['messages'].split(",")
    consensus, msa = poa(x)
    db.createMsa('knx',consensus)
    #print(consensus)

print ("Algorithm run successfully")