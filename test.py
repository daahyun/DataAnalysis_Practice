import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel('~/Documents/GitHub/DataAnalysis_Practice/pfb.xlsx') 
print(df1)

fig, axes = plt.subplots(1, 1) 
plt.plot(df1['date'], df1['sl'])
plt.xlabel('Date')
plt.ylabel('Stress level')
plt.show()

#실제 E4데이터 모으기
#시계열 데이터 추출
#두개 선 그래프 그리기
