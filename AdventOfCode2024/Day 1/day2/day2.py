# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:10:09 2024

@author: Adrian
"""

'''
CRITERIA

- Criterion 1: Any two adjacent levels differ by at least one and at most three
- Criterion 2: The levels are either all increasing or all decreasing.
'''

import numpy as np

#arr = np.loadtxt('test_data.txt', dtype='int')

with open('input.txt', 'r') as f:
    # Read each line and split it into a list of integers
    data = [list(map(int, line.split())) for line in f]

# Convert the list of lists into a NumPy array with dtype=object
arr = np.array(data, dtype=object)

print(arr[0,0])
'''
diff = arr[:,1:] - arr[:,0:-1] 
print(diff)

## Criteria 1
# Remove any elements >2, and <-2
arr1 = diff * (diff <= 2) * (diff >= -2)
print('\n')
print(arr1)

# Change all 1s --> 2s
arr1 = arr1 + arr1 * (arr1%2)
print('\n')
print(arr1)

## Criteria 2
diff2 = arr1[:,1:] + arr1[:,0:-1] 
print('\n')
print(diff2)
    
straightTrend = abs(np.sum(diff2, axis=1)) == 12

totalSafe = np.sum(straightTrend)

'''