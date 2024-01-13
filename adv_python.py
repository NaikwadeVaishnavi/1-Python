# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:29:58 2023

@author: vaish
"""


#list comprehenssion
lst=[]
for i in range(0,20):
    lst.append(i)
print(lst)

#instead of above code we can use following  concept of list comprehenssion
lst=[num for num in range(0,20)]
print(lst)

#capitalize() used to capitalized
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)

#list comorehenssion with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

lst=[f"{x}{y}" for x in range(3) for y in range(3)]
print(lst)


#set comprehenssion
lst={
     x
     for x in range(3)
     }
print(lst)

#dict comprehenssion
dict={x:x*x for x in range(3)}
print(dict)

#Generator
'''
It is another way of creating iterators in a simple way where it in a defined 
function Generators are implemented using a function
'''

#tuple comprehenssion
'''
#for tuple comprehenssion it will create object here we use generator instead of
range() cause obj is created

*when ur going to use tuple comprehenssion,one obj will get created & 
u can accesss value of that obj using for loop
'''
gen=(x 
     for x in range(3)    
     )
print(gen)
for num in gen:
    print(num)

#next() - used to show the obj step by step  (Access obj)
gen=(x 
     for x in range(3)    
     )
next(gen)
next(gen)
next(gen)

'''
for list dict set we dont see obj creation  bt for tuple it is created 
thats why tuple are not use for comprehenssion
'''
#fun which return multiple value
def range_even(end):
    for num in range(0,end,2):
        yield num 
#to return multiple value we use 'yield' here 'return' statement gives error
for num in range_even(6):
#take multiple arg using for loop (0-6 here) to return multiple value 
    print(num)
    
    
#function as an generator here function will not going to create any obj
#instead of for loop we can write our own generator

gen=range_even(6)
next(gen)
next(gen)
next(gen)

#chaining generator 
#encrypt password
def length(itr):
    for ele in itr:
        yield(len(ele))
def hide(itr):
    for ele in itr:
        yield ele*'*'
#here ele* means all the ele char and it will get conveted into "*" for encryption purpose
passwords=['not-good',"give'm-pass",'00100=100']
 
for password in hide(length(passwords)):
    print(password)

#enumerate
#printing list with index
lst=['milk','egg','bread']
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")
#same code can be implemented using enumerate 
lst=['milk','egg','bread']
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")


#password generator and its encryption(check again)

import string
adjective=['sleepy','hot','smelly','slow','fat','tall','small','fear']
noun=['apple','dianosor','goat','cow','cat','dog','panda','horse']
import random
nouns=random.choice(noun)
adjectives=random.choice(adjective)
number=random.randrange(0,100)
special_char=random.choice(string.punctuation)
password=adjectives+nouns+str(number)+string.punctuation
print('Your new password is:%s' %password)


#program to check pasword is strong or weak
'''
conditions
at least 8 char
at least one uppercase
one lowercase
'''
def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
#check each char in the password and see which requirement meets
    for ch in password:
        if ch>="A"and ch<="Z":
            has_upper=True
        elif ch>="a" and ch<="z":
            has_lower=True
        elif ch>="0" and ch<="9":
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
p=input("Enter ur password : ") 
if checkPassword(p):
    print("Strong password")
else:
    print("Weak password")
def length(itr):
    for ele in itr:
        yield(len(ele))
def hide(itr):
    for ele in itr:
        yield ele*'*'
#here ele* means all the ele char and it will get conveted into "*" for encryption purpose
passwords=['not-good',"give'm-pass",'00100=100']
 
for password in hide(length(passwords)):
    print(password)

#find all num in range 1-1000 divisible by 7
for i in range(1,1000):
    if(i%7==0):
        print(i,end=' ')

div7=[num for num in range(1000) if(num%7==0)]
print(div7)

#find all num from 1-1000 that have num 3 in them
three=[num for num in range (0,1000) if  '3' in str(num)]
print(three)

#count num of spaces in str
s="Asdsx sdvcx waeds dsadx"
space=[space for space in s if space==' ']
print(len(space))

#create a  list of all consonant in the string 
#"Yellow yank like yelling and yawning and yesterday they yodled while eating yuky yams"

sentence='''Yellow yank like yelling and yawning 
and yesterday they yodled while eating yuky yams'''

result=[letter for letter in sentence if letter not in 'a,e,i,o,u," "'] 
print(result)

#find the common num in 2 list without using set n tuple
list_a=[1,2,3,4,5]
list_b=[2,3,4,5]
common=[a for a in list_a if a in list_b]
print(common)

'''
get only the numbers in a sentence like 
'In 1984 there were 13 instaces of protest with over 1000 people attending '
'''
#isalpha() - used to check the alphabets  are present or not

sentence='In 1984 there were 13 instaces of protest with over 1000 people attending'
word=sentence.split(" ")
result=[num for num in word if not num.isalpha()]
print(result)

'''
given numers=range(20) produce a list  containing a word even if num is odd 
return word 'odd'

'''
result=[]
for i in range(20):
    if i%2==0:
        result.append("even")
    else:
        result.append("odd")
print(result)

#using list comprehenssion

#if u need to write else condition in list comprehenssion then u need to write for loop on left side
#u have to write if-else block first n then for loop 
result=['even' if i%2==0 else 'odd' for i in range(20)]
print(result)


'''
product a list of tuples consisting of only 
the matching numbers in these lists list_=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
result would like(4,4) ,(12,12)
'''
list_=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
result=[(a,b) for a in list_a for b in list_b if a == b]
print(result)

#assignment 
'''
take 2 sentence and print matching word like above
'''
#find all words length less than 4
sentence='on summer day ramnath sonar went swimming in the sun and his red skin stung'
examine=sentence.split(" ")
result=[word for word in examine if len(word)<=4 ]
print(result)

#write program to print a specified list after removing 0th and 4th 5th element
color=['red','green','white','black','pink','yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


#program that creates a generator function that yield cube of num from 1-n accept n from user

def cube_generator(n):
    for i in range(1,n):
        yield i**3
        
#accept input from user    
  
n=int(input("Enter num : "))
#create the generator object
cubes=cube_generator(n) #object
print("Cubes of numbers from n-1 : ",n)
#iteration over the generator and print cubes
for num in cubes:
    print(num)


#program to implement a generator that generates random number within given range
import random
def random_num_generator(star,end):
    while True:
        yield random.randint(start,end)
#accept input
start=int(input("Enter start val :"))
end=int(input("Enter end val : "))
#create  generator object
random_num=random_num_generator(start,end)

#generate and print 10 random num  
print("Random number between",start," and ",end)
for _ in range(10):
    print(next(random_num))

#program to generate 3*4*6 3D array whose each element is * 3=ROWS 4,6==COL
array=[[['*' for col in range(6)]for col in range (4)]for row in range(3)]
print(array)

#print num of specified list after removing even num from it
num=[7,8,120,25,44,20,27]
num=[x for x in num if x%2!=0]
print(num)
