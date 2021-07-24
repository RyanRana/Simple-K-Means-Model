from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.rand(1,8)
x2 = np.random.rand(1,8)

X = np.array(list(zip(x1, x2))).reshape(len(x1), 2

plt.plot() 
plt.scatter(x1, x2) 
plt.show() 

distortions =[]
inertias =[]
mapping1 ={}
mapping2 ={}
K = range(1, 11)
for i in K:
kmeanModel =KMeans(n_clusters=k).fit(X)
kmeanModel.fit(X)
distortions.append(sum(np.min(cdist(X,kmeanModel.cluster_centers_,'euclidean'), axis=1)) / X.shape[0])
inertias.append(kmeanModel.inertia_)
mapping1[k] = sum(np.min(cdist(X,kmeanModel.cluster_centers_,'euclidean'), axis=1)) / X.shape[0]
mapping2[k] = kmeanModel.inertia_

plt.plot(K, inertias, 'bx-')
plt.show() 
