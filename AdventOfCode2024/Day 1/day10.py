# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:47:28 2024

@author: Adrian
"""

import numpy as np

map_str = np.loadtxt('inputTest.txt', dtype='str')
#map_str = np.loadtxt('input.txt', dtype='str')

print(map_str)

#print(arr)
#print(len(arr))
#print(len(arr[0]))
heights = np.array([])

for line in map_str:
    line_int = np.array([])
    
    for char in line:
        #print(char)
        line_int = np.append(line_int, int(char))
    
    heights = np.append(heights, line_int, axis=0)

heights = np.reshape(heights, (len(map_str), len(map_str[0])))


#print(line_int)
print(heights)


