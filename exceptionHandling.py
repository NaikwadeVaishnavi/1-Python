# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:20:06 2023

@author: vaish
"""

#exception are handled and solved bt error cannt

#zero division error
a=int(input("NUM:"))
b=int(input("Num2:"))
try:
    print(a/b)
except ZeroDivisionError:
    print("Exception occur cant divide by 0")

'''
need for encoding 
Introduction to Unicode
Definitions
Unicode Transformation Format(UTF)
 Today’s programs need to be able to handle a wide variety of characters.
 Applications are often internationalized to display messages and output
 in a variety of user-selectable languages; the same program might need 
 to output an error message in English, French, Japanese, Hebrew, or Russian. 
 Web content can be written in any of these languages and can also include 
 a variety of emoji symbols. Python’s string type uses the Unicode Standard 
 for representing characters, which lets Python programs work with all these 
 different possible characters.
'''

#file not found error
filename="alice.txt"
with open (filename,encoding='utf-8') as file:
           contents=file.read()
           
#exception handling
filename="alice.txt"
try:
    with open (filename,encoding='utf-8') as file:
               contents=file.read()
except FileNotFoundError:
    print("Cann't read this file as it is not exist")

#storing data
'''
many of ur program will ask user to input certain kind of information .
u might allow users to preferences or details  in that case u have to store info
a simple way do this is JSON

JSON- JavaScript Object Notation 
was inspired by a subset of the JavaScript programming language 
dealing with object literal syntax. 

format was origianlly  in form of dictionary 
support premitives called string,object, array
json is JAVA package in  python
'''

import json
numbers=[2,3,4,5,6,7]
filename='numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)

import json
username="vaishnavi"
filename="username.json"
with open(filename,'w') as f:
    json.dump(username,f)
print(f"We'll remember u when u come back,{username}")

'''
now lets write a new program that greets a user whose name has already exist 
and data is stored
'''
import json 
filename='username.json'
with open(filename) as f:
    usrename=json.load(f)
print(f"Welcom back{username}")

'''
load the username if it has been stored previously
otherwise prompt a username and store it
'''
filename='username.json'
try:
    with open(filename) as f:
        usrename=json.load(f)
except FileNotFoundError:
    username=input("What is ur name:")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"We'll rember u when u come back,{username}")
else:
    print(f"Welcom back{username}")
        
    