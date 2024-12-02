# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:10:09 2024

@author: Adrian
"""

import numpy as np
from functions import *

df = pd.read_csv('test_data.txt', sep=' ', header=None)

print(df)
print('\n')
print(df.iloc[:,0:-1])
print('\n')
print(df.iloc[:,1:])
diff = df.diff()
diff = df.iloc[:,0:-1].subtract(df.iloc[:,1:])

print(diff)