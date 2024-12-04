# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:30:44 2024

@author: Adrian
"""

'''
Read XMAS in 8 directions:
    L --> R
    R --> L
    Up --> Down
    Down --> Up
    Diagonal LU --> RD
    Diagonal RU --> LD
    Diagonal LD --> RU
    Diagonal RD --> LU
'''
'''
IDEA:
    For loop through the entire string.
    When an 'X' is found halt, perform 8 checks:
        is_LR()
        is_RL()
        is_UD()
        is_DU()
        is_LU_RD()
        is_RU_LD()
        is_LD_RU()
        is_RD_LU()
    count += is_check()
    
    How to handle edge cases?
    
    str_len = len('XMAS')
    
    x, y
        is_LR(x, y): if x < len(x_dir) - str_len
        is_RL(x, y): if x > str_len
        is_UD(x, y): if y < len(y_dir) - str_len
        is_DU(x, y): if y > str_len
        is_LU_RD(x, y): if x < len(x_dir) - str_len AND y < len(y_dir) - str_len
        is_RU_LD(x, y): if x > str_len AND y < len(y_dir) - str_len
        is_LD_RU(x, y): if x < len(x_dir) - str_len AND y > str_len
        is_RD_LU(x, y): if x > str_len - str_len AND y > str_len
'''

'''
def is_RL(x, y): if x > str_len
def is_UD(x, y): if y < len(y_max) - str_len
def is_DU(x, y): if y > str_len
def is_LU_RD(x, y): if x < len(x_max) - str_len AND y < len(y_max) - str_len
def is_RU_LD(x, y): if x > str_len AND y < len(y_max) - str_len
def is_LD_RU(x, y): if x < len(x_max) - str_len AND y > str_len
def is_RD_LU(x, y): if x > str_len - str_len AND y > str_len
'''


def is_LR(r, c, my_list, r_max, c_max, word): 
    
    if c <= (c_max - len(word)):
        if (my_list[r][c+1] == word[1]) and (my_list[r][c+2] == word[2]) and (my_list[r][c+3] == word[3]):
            
            return 1
        
def is_LR(r, c, my_list, r_max, c_max, word): 
    
    if c <= (c_max - len(word)):
        if (my_list[r][c+1] == word[1]) and (my_list[r][c+2] == word[2]) and (my_list[r][c+3] == word[3]):
            
            return 1

file_path = 'input.txt'

with open('input.txt', 'r') as file:
    words = file.readlines()

word = 'XMAS'

words = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX'
    ]

#words = ['abc', 'dXf']

i = 0

for row in range(0, len(words)):
    for col in range(0, len(words[0])):
        #print(row, col, words[row][col])
        if words[row][col] == 'X':
            if is_LR(row, col, words, len(words[0]), len(words), word):
                print('LR at:', row, col)
                i += 1
print(i)
