# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:44:50 2022

find methods for strings
"""

s= "here is a random string that I am going to be searching and finding a part of"

index = s.find("finding")
print(index)

index = s.find("Finding") #search is case sensitive
print(index)

if "search" in s:
    print("found search\n")
else:
    print("'search' not found")
    
index = s.find("a") # will only find the first index.
print(index)


#example user input search terms.
print("Enter string of choice\n")
s=input()
print("Enter search term")
innn = input()
print(s.find(innn))