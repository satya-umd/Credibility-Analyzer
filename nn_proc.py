import pandas
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import category_encoders as ce
import matplotlib.pyplot as plt
from kmodes.kmodes import KModes
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
# le =  ce.OneHotEncoder(return_df=False, impute_missing=False, handle_unknown="ignore")
df=pd.read_csv('reps.csv', sep=',',header=0)
# my_data = genfromtxt('reps.csv', delimiter=',')
df_new = pd.DataFrame()
df = df[1:100000]
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

print("Started Clustering")
km = KModes(n_clusters=4, init='Huang', n_init=5, verbose=0)
clusters = km.fit_predict(dfc)
lda = LDA(n_components=2) #2-dimensional LDA
lda_transformed = pd.DataFrame(lda.fit_transform(dfc, clusters))
plt.scatter(lda_transformed[clusters==0][0], lda_transformed[clusters==0][1], label='Class 1', c='red')
plt.scatter(lda_transformed[clusters==1][0], lda_transformed[clusters==1][1], label='Class 2', c='blue')
plt.scatter(lda_transformed[clusters==2][0], lda_transformed[clusters==2][1], label='Class 3', c='green')
plt.scatter(lda_transformed[clusters==3][0], lda_transformed[clusters==3][1], label='Class 4', c='cyan')
plt.legend(loc=3)
plt.show()
# 3d view
# lda = LDA(n_components=3) #2-dimensional LDA
# lda_transformed = pd.DataFrame(lda.fit_transform(dfc, clusters))
# fig = pyplot.figure()
# ax = Axes3D(fig)
# ax.scatter(lda_transformed[clusters==0][0], lda_transformed[clusters==0][1],lda_transformed[clusters==0][2], label='Class 1', c='red')
# ax.scatter(lda_transformed[clusters==1][0], lda_transformed[clusters==1][1],lda_transformed[clusters==1][2], label='Class 2', c='blue')
# ax.scatter(lda_transformed[clusters==2][0], lda_transformed[clusters==2][1],lda_transformed[clusters==2][2], label='Class 3', c='green')
# ax.scatter(lda_transformed[clusters==3][0], lda_transformed[clusters==3][1],lda_transformed[clusters==3][2], label='Class 4', c='cyan')
# ax.legend(loc=3)
# pyplot.show()

