# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:15:55 2024

@author: Adrian
"""

def get_blocks(input):
    block = ''
    
    for i in range(0, len(input), 2):
        
        for j in range(0, int(input[i])):
            block += str(i//2)
        
        # If string len is odd, need a check to not run this for the last number in teh sequence
        if i + 1 < len(input):
            for j in range(0, int(input[i+1])):
                block += '.'
    
    return block

def move_blocks(input): return 0

def get_checksum(): return 0

input = '2333133121414131402'
input = '233'

blocks = get_blocks(input)
print(blocks)
# OUTPUT: 00...111...2...333.44.5555.6666.777.888899

print(blocks.count('.'))
num_ints = len(blocks) - blocks.count('.')

ordered = 0
idx = 0

while ordered < num_ints:
    if blocks[idx] != '.':
        idx += 1
        ordered += 1
    else:
        SWAP
        ordered += 1

