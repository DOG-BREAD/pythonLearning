# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:36:10 2022

inheritance

"""

class Animal():
    reproduction = " has milk"

class Dog(Animal):
    limbs =4
    
class breed(Dog):
    breed = "German shepard "
    
toby = breed()
print("Toby is a ",toby.breed," he is a Dog. \n Dogs have ",toby.limbs," limbs. Becuase toby is an animal he is fed milk as a baby")