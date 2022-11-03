# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 23:52:27 2022

nested loops
"""
x=0
y=0
for x in range(3):
    print("\n")#,x, ": ",end=" ")
    for y in range(3):
        print(y, end=" ")
        
#each person meets each other, inefficiently , all possibilites

persons = [ "John", "Marissa", "Pete", "Dayton" ]

for x in persons:
    for y in persons:
        if x != y:
            print(x," meets ",y)