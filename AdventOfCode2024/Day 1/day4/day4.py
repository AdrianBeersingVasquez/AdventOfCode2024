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
    
    str_len = length of XMAS
    
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
def is_LR(x, y): if x < len(x_max) - str_len
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

def is_RL(r, c, my_list, r_max, c_max, word):
    
    if c >= (len(word)-1):
        if (my_list[r][c-1] == word[1]) and (my_list[r][c-2] == word[2]) and (my_list[r][c-3] == word[3]):
            
            return 1

def is_UD(r, c, my_list, r_max, c_max, word):
    
    if r < (r_max - len(word)):
        if (my_list[r+1][c] == word[1]) and (my_list[r+2][c] == word[2]) and (my_list[r+3][c] == word[3]):
            
            return 1

def is_DU(r, c, my_list, r_max, c_max, word):
    
    if r >= (len(word)-1):
        if (my_list[r-1][c] == word[1]) and (my_list[r-2][c] == word[2]) and (my_list[r-3][c] == word[3]):
            
            return 1

def is_LU_RD(r, c, my_list, r_max, c_max, word):
    
    if c <= (c_max - len(word)) and r < (r_max - len(word)):
        if (my_list[r+1][c+1] == word[1]) and (my_list[r+2][c+2] == word[2]) and (my_list[r+3][c+3] == word[3]):
            
            return 1

def is_RU_LD(r, c, my_list, r_max, c_max, word):
    
    if c >= (len(word)-1) and r < (r_max - len(word)):
        if (my_list[r+1][c-1] == word[1]) and (my_list[r+2][c-2] == word[2]) and (my_list[r+3][c-3] == word[3]):
            
            return 1

def is_LD_RU(r, c, my_list, r_max, c_max, word):
    
    if c <= (c_max - len(word)) and r >= (len(word)-1):
        if (my_list[r-1][c+1] == word[1]) and (my_list[r-2][c+2] == word[2]) and (my_list[r-3][c+3] == word[3]):
            
            return 1

def is_RD_LU(r, c, my_list, r_max, c_max, word):
    
    if c >= (len(word)-1) and r >= (len(word)-1):
        if (my_list[r-1][c-1] == word[1]) and (my_list[r-2][c-2] == word[2]) and (my_list[r-3][c-3] == word[3]):
            
            return 1


file_path = 'input.txt'

with open('input.txt', 'r') as file:
    words = file.readlines()

word = 'XMAS'

'''
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
'''

#words = ['abc', 'dXf']

i = 0
for row in range(0, len(words)):
    for col in range(0, len(words[0])-1):
        #print(row, col, words[row][col])
        if words[row][col] == 'X':
            #print(row, col)
            if is_LR(row, col, words, len(words[0]), len(words), word):
                #print('LR at:', row, col)
                i += 1
            if is_RL(row, col, words, len(words[0]), len(words), word):
                #print('RL at:', row, col)
                i += 1
            if is_UD(row, col, words, len(words[0]), len(words), word):
                #print('UD at:', row, col)
                i += 1
            if is_DU(row, col, words, len(words[0]), len(words), word):
                #print('DU at:', row, col)
                i += 1
                
            if is_LU_RD(row, col, words, len(words[0]), len(words), word):
                #print('LU_RD at:', row, col)
                i += 1
            if is_RU_LD(row, col, words, len(words[0]), len(words), word):
                #print('RU_LD at:', row, col)
                i += 1
            if is_LD_RU(row, col, words, len(words[0]), len(words), word):
                #print('LD_RU at:', row, col)
                i += 1
            if is_RD_LU(row, col, words, len(words[0]), len(words), word):
                #print('RD_LU at:', row, col)
                i += 1

###############################################################################

def is_XLR(r, c, my_list, word):
    
    if (my_list[r-1][c-1] == 'M' and my_list[r+1][c-1] == 'M' and my_list[r-1][c+1] == 'S' and my_list[r+1][c+1] == 'S'):
        return 1

def is_XRL(r, c, my_list, word):
    
    if (my_list[r-1][c-1] == 'S' and my_list[r+1][c-1] == 'S' and my_list[r-1][c+1] == 'M' and my_list[r+1][c+1] == 'M'):
        return 1
    
def is_XUD(r, c, my_list, word):
    
    if (my_list[r-1][c-1] == 'M' and my_list[r+1][c-1] == 'S' and my_list[r-1][c+1] == 'M' and my_list[r+1][c+1] == 'S'):
        return 1
    
def is_XDU(r, c, my_list, word):
    
    if (my_list[r-1][c-1] == 'S' and my_list[r+1][c-1] == 'M' and my_list[r-1][c+1] == 'S' and my_list[r+1][c+1] == 'M'):
        return 1
    
# Only need to run the code from x=1 to len - x
# similarily y can also use the same border

# no need to check whether r, c are outside the border

j = 0
for row in range(1, len(words)-1):
    for col in range(1, len(words[0])-2):
        #print(row, col, words[row][col])
        if words[row][col] == 'A':
            if is_XLR(row, col, words, word):
                j += 1
            if is_XRL(row, col, words, word):
                j += 1
            if is_XUD(row, col, words, word):
                j += 1
            if is_XDU(row, col, words, word):
                j += 1

print('Number of XMAS\'s:', i)

print('Number of X-MAS\'s:', j)

