# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:31:29 2019

@author: Sanjana
"""

#import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'C:\Users\Sanjana\Desktop\SE.csv') #for an earlier version of Excel, you may need to use the file extension of 'xls'
df['Date'] = pd.to_datetime(df['Date'])

res_time=df.groupby(df['Date'].dt.strftime('%B'))['Occur'].sum()
res_df = pd.DataFrame({'Month':res_time.index, 'Frequency of Usage':res_time.values})
Y = res_df.loc[:,'Month']
X = res_df.loc[:,'Frequency of Usage']
y_pos = np.arange(len(Y))

plt.figure(figsize=(15,4))
plt.bar(y_pos, X, align='center', alpha=0.5)
plt.xticks(y_pos, Y)
plt.ylabel('Frequency of Usage')
plt.title('Monthly Usage by Seed Entrepreneur')

plt.show()

