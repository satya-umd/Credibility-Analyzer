import os
import keras
import metrics
from sklearn import metrics
import numpy as np
import pandas as pd
import keras.backend as K
from sklearn import preprocessing
from time import time
import SimpSOM as sps

df=pd.read_csv('input_100K.csv', sep=',',header=0)
df = df.iloc[1:100]
df_new = pd.DataFrame()
dfc = np.array([])
for key in df.keys():
    categories = np.array(list(set(df[key].astype(str).values))).reshape(-1,1)
    print(len(categories))
    if(len(categories)<10000):
        le = preprocessing.OrdinalEncoder()
        # le =  ce.OneHotEncoder(return_df=False, impute_missing=False, handle_unknown="ignore")
        df_new = pd.concat([df_new, df[key]], axis=1)
        # dfc1 = le.fit_transform(df_new[key].fillna('0').values)
        dfc1 = le.fit_transform(df_new[key].fillna('0').astype(str).values.reshape(-1,1))
        if(dfc.size==0):
            dfc = dfc1
        else:
            dfc = np.concatenate((dfc, dfc1), axis=1)

raw_data = dfc

#Build a network 20x20 with a weights format taken from the raw_data and activate Periodic Boundary Conditions. 
net = sps.somNet(20, 20, raw_data, PBC=True)

#Train the network for 10000 epochs and with initial learning rate of 0.01. 
net.train(0.01, 10000)

#Save the weights to file
net.save('filename_weights')

#Print a map of the network nodes and colour them according to the first feature (column number 0) of the dataset
#and then according to the distance between each node and its neighbours.
net.nodes_graph(colnum=0)
net.diff_graph()

df=pd.read_csv('labels.csv', sep=',',header=0)
labels = df.iloc[0:100].values.flatten()
#Project the datapoints on the new 2D network map.
net.project(raw_data, labels=labels)

#Cluster the datapoints according to the Quality Threshold algorithm.
net.cluster(raw_data, type='qthresh')