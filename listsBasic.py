# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:14:25 2022

lits operations append and pop
"""

y=[6,4,2]

y.append(12)
y.append(8)
y.append(4)

print(y)

y[1] =3
print(y)


#sorting lists
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]

#sort on the first element

def get1(x):
    return x[0]

x.sort(key=get1)
print(x)

#sort by second element
def get2(x):
    return x[1]

x.sort(key=get2)
print(x)