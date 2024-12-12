# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:15:55 2024

@author: Adrian
"""
import sys

sys.set_int_max_str_digits(0)

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

def move_blocks(input):
    
    num_ints = len(blocks) - blocks.count('.')

    idx_inc = 0
    idx_dec = len(blocks)-1

    blocks_ordered = ''
    
    while idx_inc < num_ints:
        if blocks[idx_inc] != '.':
            blocks_ordered += blocks[idx_inc]
        
        else: # Perform a swap
            # Run backwards through string, finding the non '.' value to substitute
            while blocks[idx_dec] == '.':
                idx_dec -= 1
                
            blocks_ordered += blocks[idx_dec]
            idx_dec -= 1
        
        idx_inc +=1
    
    return blocks_ordered

def get_checksum(sequence): 
    
    checksum = 0
    for i in range(0, len(sequence)):
        checksum += i * int(sequence[i])
    
    return checksum

with open('input.txt', 'r', encoding='utf-8') as file:
    input = file.read()

#input = '2333133121414131402'
#input = '123'

blocks = get_blocks(input)
#print(blocks)

ordered_blocks = move_blocks(blocks)
#print(ordered_blocks)

checksum = get_checksum(ordered_blocks)
print(checksum)
