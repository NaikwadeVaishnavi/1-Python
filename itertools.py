# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:35:47 2023

@author: vaish
"""

'''
program to crete iterator from several iterables in a 
sequence & display type element of new iterator
'''
#chain() - itertools 

#chain fun for list
from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#list
result=chain_func([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print("Type of new iterator",type(result))

print("element of new iterator")
for i in result:
    print(i,end=' ')



#chain fun for tuple
from itertools import chain
def chain_func(tup1,tup2,tup3):
    return chain(tup1,tup2,tup3)
#list
result=chain_func((1,2,3),('a','b','c','d'),(4,5,6,7,8,9))
print("Type of new iterator",type(result))

print("element of new iterator")
for i in result:
    print(i,end=' ')


'''
program that generates running product of an element in an iterable
'''
#itertool.accumulate 
'''
takes 2 arg iterable target & function which would b follwed at each iteration 
value of a target if no function is passed then by default addition 
takes place
'''
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
result=running_product([1,2,3,4,5,6,7])
for i in result:
    print(i)

#accumulator= default addition case 
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst)
result=running_product([1,2,3,4,5,6,7])
for i in result:
    print(i)

#tuple
#accumulator= default addition case 
from itertools import accumulate
import operator
def running_product(tup):
    return accumulate(tup)
result=running_product((1,2,3,4,5,6,7))
for i in result:
    print(i)

'''
program to construct an infinite iterator that return evenly
spaced value starting with the specified num and step
'''
import itertools as it
start= 10
step=1
print("Starting number is ",start," step is ",step,"")
my_counter=it.count(start,step)
print("The said function print never ending items: ")
#it will print infinite loop
for i in my_counter:
    print(i)

#prpgram to generate an infinite cycle of ele from iterable 
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)

#list
result=cycle_data(["A","B","C","D"])
print("The said function print never ending items: ")
for i in result:
    print(i)
    
#string
result=cycle_data("Python itertools")
print("The said function print never ending items: ")
for i in result:
    print(i)

'''
program to make an iterator that drops an element from the iterable 
as soon as an element is positive num
'''
import itertools as it 
def drop_while(nums):
    return it.dropwhile(lambda x: x<0,nums)
nums=[-1,-2,-3,-4,1,2,4,]
print("Original list ",nums)
result=drop_while(nums)
print("\nResultant list (drops ele from iterable when +ve num arises )\n",list(result))
