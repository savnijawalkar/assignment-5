# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:54:09 2022

@author: Dell
"""

n = int(input("Enter number of rows:"))
k = 65
for i in range(n):
    for j in range(i+1):
        print(chr(k), end=" ")
        k = k + 1
    print()
