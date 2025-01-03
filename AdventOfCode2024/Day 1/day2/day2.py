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

#with open('input.txt', 'r') as f:
    # Read each line and split it into a list of integers
#    data = [list(map(int, line.split())) for line in f]

with open('input.txt') as f:
    file = f.read()

file1 = """5 6 7 10 13 16 13
19 21 24 27 28 28
16 18 20 21 23 25 29
44 46 48 49 52 55 56 62
51 52 53 50 52
10 11 12 13 15"""

file1 = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

reports = file.split('\n')

totalSafe = 0

for report in reports:
    nums = np.array(report.split(' '), dtype=('int'))
    
    # Put a for loop here, removing one of the elements in nums each time. If 
    # any removal returns True on both checks, increment totalSafe and break
    for i in range(0, len(nums)):
        diff1 = np.concatenate((nums[0:i], nums[i+1:]), axis=0)
    
        diff = diff1[1:] - diff1[:-1]
    
        check1 = np.abs(diff).min() > 0 and np.abs(diff).max() <= 3
        check2 = sum(abs(diff)) == abs(sum(diff))
    
        if check1 and check2:
            totalSafe +=1
            break
    
    #print(nums)
    #print(diff)

print(totalSafe)


'''
Method 2: Does not work for input given it has different number of columns
diff = arr[:,1:] - arr[:,0:-1] 
print(diff)

## Criteria 1
# Remove any elements >2, and <-2
arr1 = diff * (diff <= 2) * (diff >= -2)
print('\n')
print(arr1)

# Change all 1s --> 2s (have a binaryy system, either +/-2 or 0)
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

"""
What did I learn?
Part 1:
Look at the input before going for an answer based on the sample data
numpy arrays cannot handle different number of columns. Need to use Nan or set 
to 0s
Would be nicer to load the data in its correct format, rather than reformat it 
with every use

Part 2:
Optimise the code to be adaptable from the start, don't end up needing to restructure

"""