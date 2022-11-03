# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:03:29 2022

basic oop / obejcts and classes using dog and cat created classes. NOTE self required to refer to class like javas this......
"""

class dog:
    
        breed ="a doggo"
        age = 0

puppy = dog()
print (puppy.breed)
puppy.breed = "golden retriever"
print( puppy.breed)

class cat:
    def __init__(self):
        self.breed =" "
        self.age = 0
        self.temperament ="cool"
        
    def getBreed(self):
        return self.breed
    
    def setBreed(self, breeds):
        self.breed = breeds
        
boots = cat()
print(boots.getBreed())
boots.setBreed("tabby")

print(boots.getBreed()) 
