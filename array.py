import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('~/Documents/GitHub/DataAnalysis_Practice/E4data/EDA_0503.csv') 
# print(data)

n_rows = len(data)
n_data = n_rows-1

columns = data.columns.values
columns[0] = 'SCR'
data.columns = columns

data.drop(0,axis=0,inplace=True)

array_data = np.array(data)
#print(array_data)

array_data = np.reshape(array_data, (-1, 4))
#print(array_data)
#print("shape: ", array_data.shape)

mean_data = np.mean(array_data, axis=1) 
print(mean_data)


