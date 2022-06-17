# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:59:46 2022

@author: Dell
"""

import math
a = int(input("Enter length of first side of the triangle:"))
b = int(input("Enter length of second side of the triangle:"))
c = int(input("Enter length of third side of the triangle:"))
s = (a+b+c)/2   # s = semi-perimeter
if a < b+c and b < a+c and c < a+b:    #checks if the sides can form a triangle.
    A = math.sqrt(s*(s-a)(s-b)(s-c))
    print("Area of the trianle is",A)
else:
    print("Not a valid triangle!")