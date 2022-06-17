# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:50:20 2022

@author: Dell
"""

lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)