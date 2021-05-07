import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel('~/Documents/GitHub/DataAnalysis_Practice/pfb.xlsx') 

date1 = {'start': pd.to_datetime('2021-04-08 11:00:00'), 'end': pd.to_datetime('2021-04-08 11:30:00')}
date2 = {'start': pd.to_datetime('2021-04-09 11:00:00'), 'end': pd.to_datetime('2021-04-09 11:30:00')}

fig, axes = plt.subplots(1,1)
plot_line(date1, axes)
plot_line(date2, axes)

def plot_line(date, ax)
    target_dataframe = df1[(df1['date'] >= target_time['start']) & (df1['date'] <= target_time['end'])]

plt.plot(df1['date'], df1['sl'])
plt.xlabel('Date')
plt.ylabel('Stress level')
plt.show()