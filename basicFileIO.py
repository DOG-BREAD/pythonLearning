# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 23:35:54 2022

read a file
"""
import os.path
from os import path

if path.exists("test.txt"): 
    f = open("test.txt")

    for x in f:
        print(x)
    f.close()
else:
    print("File does not exist")
    
f = open("test.txt", "a")
f.write("Here is some random stuff I am appending\n")
f.close()