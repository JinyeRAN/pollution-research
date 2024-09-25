from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

data = np.loadtxt(r'H:\U\new_workfile\trend.txt')
data_x = data

data_zs = (data_x-data_x.mean())/data_x.std()
scale = MinMaxScaler().fit(data_x)
data_datascale = scale.transform(data_x)

for num in range(5, 25):
    kmeans = KMeans(n_clusters=num, random_state=123, max_iter=30000, init='k-means++').fit(data_datascale)
    r_new = pd.concat([pd.DataFrame(data_x), pd.Series(kmeans.labels_)], axis=1)
    nut = kmeans.inertia_
    path_out = 'C:\\Users\\Ran JY\\Desktop\\kt\\'+str(num)+'类'+str(nut)+'.xlsx'
    r_new.to_excel(path_out)
