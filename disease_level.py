# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:50:03 2019

@author: Sanjana
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\Sanjana\Desktop\LF.csv')
df_bottom = pd.read_csv(r'C:\Users\Sanjana\Desktop\bottom_users_kenya.csv')
df_top = pd.read_csv(r'C:\Users\Sanjana\Desktop\top_users_kenya.csv')

avg_disease_prob = [0] * 20

df_top['avg_disease_prob'] = avg_disease_prob
df_bottom['avg_disease_prob'] = avg_disease_prob

for i in range(2932):
    for j in range(20):
        if(df.loc[i,'User Name']==df_top.loc[j,'User Name']):
            df_top.loc[j,'avg_disease_prob'] = (df_top.loc[j,'avg_disease_prob'] + df.loc[i,'Disease Probability'])
        if(df.loc[i,'User Name']==df_bottom.loc[j,'User Name']):
            df_bottom.loc[j,'avg_disease_prob'] = (df_bottom.loc[j,'avg_disease_prob'] + df.loc[i,'Disease Probability'])
            


df_top.to_csv(r'C:\Users\Sanjana\Desktop\top_users_kenya.csv')
df_bottom.to_csv(r'C:\Users\Sanjana\Desktop\bottom_users_kenya.csv')        
    

