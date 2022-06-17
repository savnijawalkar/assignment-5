# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:54:24 2022

@author: Dell
"""

print("Prime numbers in an input range.")
start = int(input("Enter starting of range(>=2):"))
end = int(input("Enter ending of range:"))
for i in range(start,end+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)