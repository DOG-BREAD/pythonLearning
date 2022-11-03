# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:02:01 2022

join method example programs
"""

#define strings

a = "AAAAAA"
b = "BBBBBB"

#define the sequence
sequence= (a,b)

#combine to make ne wstring , space character as break points, can be any character
word = " ".join(sequence)
print(word)

#join method also works with lists/ arrays 
#format is as 
x = ["How", "Can", "It", "Be", "So", "Simple"]

y = "".join(x)
print(y)