# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:14:56 2019

@author: Sanjana
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\Sanjana\Desktop\Kenya_PlantVillage.csv') #for an earlier version of Excel, you may need to use the file extension of 'xls'
word_grouping = df[['User Name','Occur']].groupby('User Name')
Occurrences_of_People = word_grouping.count().reset_index()
top_few = Occurrences_of_People.nlargest(20, ['Occur'])
bottom_few = Occurrences_of_People.nsmallest(20, ['Occur'])
print (Occurrences_of_People)

Occurrences_of_People.to_csv(r'C:\Users\Sanjana\Desktop\users_kenya.csv')
top_few.to_csv(r'C:\Users\Sanjana\Desktop\top_users_kenya.csv')
bottom_few.to_csv(r'C:\Users\Sanjana\Desktop\bottom_users_kenya.csv')
#l=len(Occurrences_of_People)
#print("Total number of Users")
#print (l)
#y_pos = np.arange(len(top_few.loc[:,'User Name']))

##f = plt.figure(figsize=(200,100))
##plt.bar(y_pos, top_few.loc[:,'Occur'], align='edge', width=20.0)
##plt.xticks(y_pos,top_few.loc[:,'User Name'])
##plt.ylabel('Frequency Usage')
#plt.title('Participants')
#f.savefig("feq_farm.pdf")
