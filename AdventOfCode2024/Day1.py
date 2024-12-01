# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:51:26 2024

@author: beers
"""

import numpy as np
import pandas as pd

df = pd.read_csv("input", delimiter='\t', header=None, names=['Data1', 'Data2'])

for col in df:
    df[col] = df[col].sort_values(ignore_index=True)

print(df.size)

#df['diff'] = [x - y for x, y in zip(df.iloc[:, 0], df.iloc[:, 1])]
    
print(df.head())

#print(df.iloc[:, 1])
#print(df.iloc[:, 0])

