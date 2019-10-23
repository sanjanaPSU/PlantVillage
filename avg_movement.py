# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:44:28 2019

@author: Sanjana
"""

import pandas as pd
import numpy as np
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0
df = pd.read_csv(r'C:\Users\Sanjana\Desktop\LF.csv')

lf_latmax = df.groupby('User Name')['Lat'].max()
lf_latmin = df.groupby('User Name')['Lat'].min()
lf_longmax = df.groupby('User Name')['Long'].max()
lf_longmin = df.groupby('User Name')['Long'].min()

lf_latdist = [0]*28
lf_longdist = [0]*28
dist = [0]*28

for i in range(28):
    #lf_latdist.index[i]=lf_latmax.index[i]
    #lf_longdist.index[i]=lf_longmax.index[i]
    lf_latdist[i] = lf_latmax[i]-lf_latmin[i]
    lf_longdist[i] = lf_longmax[i]-lf_longmin[i]
    a = sin(lf_latdist[i] / 2)**2 + cos(lf_latmax[i]) * cos(lf_latmin[i]) * sin(lf_longdist[i] / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    dist[i] = R * c

print(dist)
    

    

