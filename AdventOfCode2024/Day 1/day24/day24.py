# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:22:54 2024

@author: beers
"""
import pandas as pd

with open('input.txt', 'r') as file:
    #data = file.readlines() # read()
    data = file.read() # read()

data = data.split('\n\n')

starting_states = data[0].split('\n')
states = {}
for line in starting_states:
    key, value = line.split(': ')
    states[key] = value
states_df = pd.DataFrame(states)

rules_ls = data[1].split('\n')
rules = {}
key=0
for line in rules_ls:
    print(line)
    input1, operation, input2, _, output = line.split(' ')
    rules[key] = {'input1': input1, 'operation': operation, 'input2': input2, 'output': output}
    key+=1
rules_df = pd.DataFrame(rules)
