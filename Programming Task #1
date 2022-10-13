# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 21:43:13 2022
Programming Task #1
Given a list of digits, determine the integer that it represents. 

For example, given the list: [8,3,5,1], your program should output 8351.

@author: YariF
"""

# The approach is :
    # figure out that the position of the number in the list helps to find its final value
    # for example for [5,1] the output is 51=50+1=5*(10**1)+1*(10**0)
    # so lest first create a list which contains the values ...(5)...(0)
    # then iterate the array and sum the partial results.
# The approach is not the most efficient, but is easy to understand and helps
# to use basic knowledge about python language

list_example=[8,3,5,1]

list_multipliers=(
    list(
        range(
            len(list_example)-1
            ,-1
            ,-1
            )
        )
    )

final_number=0

for digit, index in zip(list_example,list_multipliers):
    print(digit)
    print(index)
    final_number=final_number+digit*(10**index)
    print(final_number)

print(final_number)
