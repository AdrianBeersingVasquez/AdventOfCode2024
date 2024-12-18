# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:47:28 2024

@author: Adrian
"""

import numpy as np
from matplotlib import pyplot as plt

map_str = np.loadtxt('inputTest.txt', dtype='str')
#map_str = np.loadtxt('input.txt', dtype='str')

print(map_str)

#print(arr)
#print(len(arr))
#print(len(arr[0]))
topo_map = np.array([])

for line in map_str:
    line_int = np.array([])
    
    for char in line:
        #print(char)
        line_int = np.append(line_int, int(char))
    
    topo_map = np.append(topo_map, line_int, axis=0)

topo_map = np.reshape(topo_map, (len(map_str), len(map_str[0])))



def my_func(travelMap, trailheadMap, num=9):
    if num == 1:
        return 0
    
    else:
        if 1:
            1
        else:
            return 0
        
#        travelMap

def UPLD_check(topo_map):
    num = 2
    
    new_topo_map = topo_map
    
    ones = np.nonzero(topo_map)
    for coord in ones:
    
    return new_topo_map

topo_map_filter = topo_map==2

ones = np.nonzero(topo_map_filter)
coord = ones[0]

points_map = np.zeros(len(map_str), len(map_str[0]))

# LEFT
points_map[coord[0]][coord[1]-1]
# RRIGHT
points_map[coord[0]][coord[1]+1]
# UP
points_map[coord[0]-1][coord[1]]
# DOWN
points_map[coord[0]+1][coord[1]]
                      
new_topo_map = 
print(ones[0])

print(ones)
#print(line_int)
#print(topo_map)

#plt.figure()
#plt.imshow(topo_map)
#plt.show()


#plt.figure()
#plt.imshow(topo_map_filter)
#plt.show()


