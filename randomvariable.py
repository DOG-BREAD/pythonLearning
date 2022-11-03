# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:40:23 2022

random numbers generator example program


"""

import random

# Create a random floating point number and print it.
print(random.random())

# pick a random whole number between 0 and 10.
print(random.randrange(0,10))

# pick a random floating point number between 0 and 10.
print(random.uniform(0,10))


x = random.random()
print(x, " ",random.random(), " " , random.random(),  " " , random.random())
