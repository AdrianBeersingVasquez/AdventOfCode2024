# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:40:27 2024

@author: beers
"""

import pandas as pd

def get_test_data():
    
    data = {
        'Column1': [3, 4, 2, 1, 3, 3],
        'Column2': [4, 3, 5, 3, 9, 3]
    }
    
    return pd.DataFrame(data)

def sort_df_cols(df):
    for col in df:
        df[col] = df[col].sort_values(ignore_index=True)
    
    return df
    