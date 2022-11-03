# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:55:43 2022

basics of functions and lists
"""

mylist = [1,2,3,4,5]

def sum(x):
    i=0
    total=0
    while(i <  len(x)):
        total+=x[i]
        i+=1
    return total

print(sum(mylist))


states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming' ] 

#program will print all the states
print(states)

for x in states:
    if x[0]=='M':
        print(x)