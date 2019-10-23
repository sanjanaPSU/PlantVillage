# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:18 2019

@author: Sanjana
"""

import pandas as pd
import datetime


df = pd.read_csv(r'C:\Users\Sanjana\Desktop\LF.csv')

for i in range(2933):
    df.iloc[i,5] = datetime.datetime.strptime(df.iloc[i,5], '%Y-%m-%d %H:%M:%S %Z').date()

avg_dateusage = df.groupby('Date')['Occur'].sum()

df_dates = pd.DataFrame(avg_dateusage)
df_dates.to_csv(r'C:\Users\Sanjana\Desktop\date_users_kenya.csv')