# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:55:12 2022

@author: Dell
"""

list=input('Enter the words in space separated format : ').split()
d={}                # dictionary to count number of occurences
for i in list:
    if i in d:      # if key already in d, then increment count by 1
        d[i]+=1
    else:           # if key not in d, then count is 1
        d[i]=1
print(d)