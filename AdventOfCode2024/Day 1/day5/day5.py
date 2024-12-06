# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:37:27 2024

@author: Adrian
"""

def get_sample_data(file):
    with open(file, 'r') as file:
        rules_and_updates = file.readlines()
    
    rules = rules_and_updates[0:21]
    updates = rules_and_updates[22:]
    
    return rules, updates
'''

For num in line, 
subsetRules = num.is_in(Rules) # subset is any rule where num appears (before and after_
Create list of X with each other number
Eg, Pairings: 
[11 44,
22 44,
33 44
44 55
44 66
X Y] etc
If Y in subsetRules: # There is a rule that corresponds to both of these numbers
Get subRule
	#If subRule == Pairing
	 #	All is well, the rule is being adhered to
	If subRule != Pairing # this is of interest
		Breaks_rule[line_idx] = True
# Now have an array containing the index of every line where there is a rule break
# Need to do: using this array, get lines where breaks_rule == False
# for i in lines[ NOT breaks_rule]:
# mid = len(line)// 2
# cum_sum += mid
11 22 33 44 55 66 77 88 99

'''

def get_rules_subset(num, rules):
    
    subset = []
    
    for rule in rules:
        if num in rule:
            num1 = int(rule[0]+rule[1])
            num2 = int(rule[3]+rule[4])
            subset.append([num1, num2])
            
    return subset

file_path = 'input.txt'

with open('input.txt', 'r') as file:
    rules_and_updates = file.readlines()

rules = rules_and_updates[0:1176] # 1175
updates = rules_and_updates[1177:]

rules, updates = get_sample_data('test_input.txt')

for line in updates:
    for char in range(0, len(line)-1, 3):
        num = line[char] + line[char+1]
        
        print(char, num)
        
        miniRules = get_rules_subset(num, rules)
    #print(len(line))

def str_to_int():
    
    
    return 0

n = 9
print(line)
print(line[:n] + line[n+3:])
str1 = '75'
miniRules = get_rules_subset(num, rules)

line_redacted = line[:n] + line[n+3:]

line_redacted_int = str_to_int(line_redacted)

#for char2 in range(0)
# ls_to_int


'''
Learnings:
    \n at the end of a file is necessary, as it counts as a (hidden) character
'''
print('\n')
