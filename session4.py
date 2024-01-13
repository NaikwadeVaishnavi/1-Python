# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:15:37 2023

@author: vaish
"""
def build_person(first_name,last_name):
    #return dict of info about person
    person={'first':first_name,'last':last_name}
    return person
musician=build_person("Vaishnavi", "Naikwade")
print(musician)

#passing list (pass list to fun )

def great_users(names):
#print simple greeting msg to each user in list
    for name in names:
        msg=f"Hello {name.title()}!"
        print(msg)
usernames=["Vasudha","Vedika","Nikita"]
great_users(usernames)


#passing arbitrary number of arg
def make_pizza(*toppings):
#print list of topping that have been requested
    print(toppings)
make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")

#now we can replace the print() call with a loop that runs through 
#the list of toppings and describe the pizza being ordered


def make_pizza(*toppings):
    for topping in toppings:
        print(f"-{toppings}")
make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")

#mixing positional and arbitrary arg
# *indicate any no of arg 
def make_pizza(size,*toppings):
   print(f"\nMaking a {size}-inch with the following toppings:")
   for topping in toppings:
       print(f"-{toppings}")
make_pizza(16,"pepperoni")
make_pizza(12,"mushrooms","green peppers","extra cheese")

'''
here we have created a  pizza.py file anf importing that file here
'''

import pizza
pizza.make_pizza(16,"pepperoni")
pizza.make_pizza(12,"mushrooms","green peppers","extra cheese")

'''
importing specific function from file
'''
from pizza import make_pizza
make_pizza(16,"pepperoni")
make_pizza(12,"mushrooms","green peppers","extra cheese")

#using 'as' to give function an alias
from pizza import make_pizza as mp
mp(16,"pepperoni")
mp(12,"mushrooms","green peppers","extra cheese")


#using 'as' to give module an alias
import pizza as p
p.make_pizza(16,"pepperoni")
p.make_pizza(12,"mushrooms","green peppers","extra cheese")

#importing all functions
from pizza import *
make_pizza(16,"pepperoni")
make_pizza(12,"mushrooms","green peppers","extra cheese")

#SCOPE of variable
'''
#this is invallid cause u need to initialise first n then define it will gove error(
NameError: name 'x' is not defined)
x=x+1
x=6
print(x)
'''
x=6
x=x+1
print(x)

'''
lambda function == anonymous function
it will be initialised when it will called after exec it will be vanished from 
memory
until it has been assigned a value
'''
#lambda function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c : a+b+c #funName=lambda arg : business logic
add(4,5,6)

def mul(a,b,c):
    mult=a*b*c
    return mult
print(mul(4,5,6))
mul=lambda a,b,c : a*b*c #funName=lambda arg : business logic
mul(4,5,6)

# here u can pass any no. of arg if arg are not known using *
val=lambda *args:sum(args)
val(1,2,3,4,5,6)
val(1,2,3,4,5,6,7,8)


#keyword (**kwargs) and non keyword (*arg)
'''
non keyword arg.
*args in function definitions in Python is used to pass a variable 
number of arguments to a function. It is used to pass a non-keyworded, 
variable-length argument list. 
'''

def person(name,**data):
    print(name)
    print(data)
person(name="Naman", age="28",place="Mumbai",mobNo="1234567890")
'''
keyword args
*kwargs in function definitions in Python is used to pass a keyworded, 
variable-length argument list. We use the name kwargs with the double star.
 The reason is that the double star allows us to pass through keyword 
  arguments (and any number of them).
'''
def person(name,**data):
    print(name)
    for i,j in data.items():    
        print(i,j)
    
person(name="Naman", age="28",place="Mumbai",mobNo="1234567890")

val=lambda **data:sum(data.values())
val(a=2,b=6,c=7,d=10)

#use if in lambda fun
'''
#following code will give error (expected 'else' after 'if' expression)
max=lambda a,b :x if(a>b)
print(max(1,2))
'''
max=lambda a,b :a if(a>b) else b
print(max(1,2))
print(max(18,2))


