# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:22:05 2022

mutliple return , aparently python can return more than one thing at a time ... thats new 
"""

#multiply and divide
x=6
y=7



def multAndDivide(x,y):
    return x+y,x*y

sums,times = multAndDivide(x,y)
print(sums," ",times)


