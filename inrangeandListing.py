# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:50:09 2022

inrange and lists
"""
list = []
for x in range(0,1001):
    list.append(x)
    
print(list)

even =[]
odd =[]

def splitEvenOdd(list):
    for x in list:
        if(x%2 ==0):
            even.append(x)
        else:
            odd.append(x)
splitEvenOdd(list)       
print(even)
print(odd)        
