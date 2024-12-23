# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 00:26:20 2024

@author: beers
"""

with open('input.txt') as f:
    file = f.read()
inc = 0
for i in range(0, len(file)):
    if file[i]=='m' and file[i+1]=='u' and file[i+2]=='l' and file[i+3]=='(':
        inc+=1
        
        get_comma_idx()
        get_bracket_idx()
        
        num1 = 0
        num2 = 0
