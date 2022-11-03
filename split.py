# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:21:51 2022

split method examples
"""
#importing regular expressions
import re

s= "it is very fabulous"
x =s.split(" ") # splits by one char delimter by defualt
print(x)

x= re.split('[vfi]',s) # splits using 'f', 'v', or 'i' as a deliemter
print(x)

s= "ititititititititttittittiiiititititititit"
x=re.split("it",s)
print(x)