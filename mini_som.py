from minisom import MiniSom
import os
import keras
import metrics
from sklearn import metrics
import numpy as np
import pandas as pd
import keras.backend as K
from sklearn import preprocessing

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

som = MiniSom(6, 6, 41, sigma=0.3, learning_rate=0.5) # initialization of 6x6 SOM
som.train_random(raw_data, 100) 
print("\n...ready!")
from pylab import plot,axis,show,pcolor,colorbar,bone
bone()
pcolor(som.distance_map().T) # distance map as background
colorbar()