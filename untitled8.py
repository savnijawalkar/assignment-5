# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:55:07 2022

@author: Dell
"""

i = 10
l = []
p = []
n = []
odd = []
even = []
Dict = {}
while i > 1:
    num = int(input("Enter integer:"))
    l.append(num)       # make an original list with user inputted integers
    i -= 1
for j in l:
    if j >= 0:          # adds to positive integers list
        p.append(j)
    if j < 0:           # adds to negative integers list
        n.append(j)
    if j % 2 != 0:      # adds to odd integers list
        odd.append(j)
    if j % 2 == 0:      # adds to even integers list
        even.append(j)
    Dict[j] = l.count(j)
print("a) Positive integers:", p)
print("b) Negative integers:", n)
print("c) Odd integers:", odd)
print("d) Even integers:", even)
print('e)')
for k in Dict:
    print(f'integer:{k} ; number of times it occurs: {Dict[k]}')