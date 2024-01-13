# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:40:31 2023

@author: vaish
"""

#use zip function = function for parallel iteration
name=['dada','mama','kaka']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

#zip function ignore the excessive element in first list it will get excluded
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip(name,info): 
    print(nm,inf)
'''
zip_longest    
it will consider excessive element whose value is not assigned 
and print it with value as none
'''

from itertools import zip_longest

name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

#here we use fillvalue to assign value instead of None
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)


#use of all(),if all values are True then it will produce output 

lst=[2,3,6,8,9]
if all(lst):
    print('all values are true')
else:
    print("Useless")
#here if value 0  and None is present in list it will print useless
lst=[2,3,6,8,9,0]
if all(lst):
    print('all values are true')
else:
    print("Useless")
    

#any()=check any non zero value
#if all 0 then useless 
lst=[0,0,0]
if any(lst):
    print('all values are true')
else:
    print("Useless")


lst=[2,3,6,8,9,0]
if any(lst):
    print('all values are true')
else:
    print("Useless")
    
#count() - itertool to measure the num of variables 
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#start counting from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#cycle() method used to perform repeatative task/periodic task

import itertools
instructions=['Eat','Code','Sleep']
for instruction in itertools.cycle(instructions):
    print(instruction)

#repeat() 
from itertools import repeat
for msg in repeat('keep patience',times=3):
    print(msg)
    
'''
#combination - combination is a way of selecting items from a collection, 
such that (unlike permutations) the order of selection does not matter.
nCr = nPr / r! 
'''
from itertools import combinations
players=['john','jani','janardhan']
for i in combinations(players, 2):
    print(i)

'''
 permutation= relates to the act of arranging all the 
 members of a set into some sequence or order. 
 nPr = (n!) / (n-r)!
 
'''
from itertools import  permutations
players=['john','jani','janardhan']
for i in  permutations(players, 2):
    print(i)
    
#product() 
from itertools import  product
team_a=['rohit','pandya','bumbrah']
team_b=['virat','manish','sami']
for pair in product(team_a,team_b):
    print(pair)


age=[27,17,21,19]
adults=filter(lambda age:age >=18,age)
print([age for age in adults ])

#shallow copy & deep copy

'''In Shallow copy, a copy of the original object is stored and
 only the reference address is finally copied. 
 In Deep copy, the copy of the original object and 
 the repetitive copies both are stored. 2. Shallow copy is faster 
 than Deep copy.
'''

list_a=[1,2,3,4,5]
list_b=list_a
#print(list_b)
#[-10,2,3,4,5]
list_a[0]=-10
print(list_a)
print(list_b)

'''
shallow copies are going to create 1 level deep copy
modifying on level 1 doesnt affect  the other list
use copy.copy()or object-specified
'''
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)
#not affecting the other list
list_b[0]=-10 #here only list_b will get changed
print(list_a)
print(list_b)
#[1, 2, 3, 4, 5] previous list
#[-10, 2, 3, 4, 5] output list

#bt with nested obj modifying on level 2 or deeper does affect the other list

import copy
list_a=[[1, 2, 3, 4, 5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affect other
list_a[0][0]=-10
'''
here there are 2 lists that  are combined to form single list 
so use a[0][0] to access first element of first list
first [0] indicates list 0(i.e.first list)
and second [0] indicate 0th element of list
 '''
print(list_a)
print(list_b)

#deep copies
'''
in shallow copies with nested objects modifying on level 2 or deeper 
does affect the other
'''

#deep copies
list_a=[[1, 2, 3, 4, 5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
#does not affect other
list_a[0][0]=-10
print(list_a)
print(list_b)
