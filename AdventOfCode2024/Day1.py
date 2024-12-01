# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:51:26 2024

@author: beers
"""

import pandas as pd
from functions import *


df = get_test_data()
df = pd.read_csv("input", sep='\s+', header=None, names=['Column1', 'Column2'])

df = sort_df_cols(df)

df['diff'] = [abs(x - y) for x, y in zip(df['Column1'], df['Column2'])]
    
totalListDiff = sum(df['diff'])

for idx, row in df.iterrows():
    
    num = row['Column1']
    print(num)
    
    count = (df['Column2'] == num).sum()
    
    df.loc[idx, 'simScore'] = count * num

totalSimScore = sum(df['simScore'])
    
print(df.head())
print('totalListDiff: ', totalListDiff)
print('totalSimScore: ', totalSimScore)
