# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:49:05 2019

@author: Sanjana
"""


import pandas as pd
#import pygmaps 
import gmplot


#mymap2 = pygmaps.maps(30.3164945, 78.03219179999999, 15)
#mymap2.draw('pygmap1.html')
 
df = pd.read_csv(r'C:\Users\Sanjana\Desktop\rosaline.csv') 
latitude_list = df.loc[:,'Lat']
longitude_list = df.loc[:,'Long']
  
gmap3 = gmplot.GoogleMapPlotter(0.525376, 34.197298, 16) 
  
#scatter method of map object  
# scatter points on the google map 
gmap3.scatter( latitude_list, longitude_list, '# FF0000', 
                              size = 40, marker = True ) 
  
# Plot method Draw a line in 
# between given coordinates 
gmap3.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 1.0) 
  
gmap3.draw(r'C:\Users\Sanjana\Desktop\map13.html' ) 

