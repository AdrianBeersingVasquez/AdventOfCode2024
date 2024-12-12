# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:43:28 2024

@author: Adrian
"""

str1 = '00..111..2222.33.....'
#for i in range(0, len(str1)):
#    print(str1[i]=='.')
idx_dec = len(str1)-1
print(idx_dec)

for i in range(0, 3):
    while str1[idx_dec] == '.':
        print('index', idx_dec)
        idx_dec = idx_dec - 1
        
    print('index outside', idx_dec)
    
    print(str1[idx_dec])


