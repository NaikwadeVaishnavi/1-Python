# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:15:37 2023
@author: vaish
"""

#add num
def myfun():
    print(x+y)
x=int(input("Enter x:"))
y=int(input("Enter y:"))
myfun()

#prime no using function (fun without arg)
def primeNo():
    for i in range(2,x):
        if x%i==0:
            return"is not prime"
            break
    return"is prime"
x=int(input("Enter num:"))
primeNo()

#prime no using function (fun with arg)
def primeNo(x):
    for i in range(2,x):
        if x%i==0:
            return("is not prime")
            break
    return("is prime")

print(primeNo(13))

#f string in function
def greatUser(username):
    print(f"Hello {username}")
greatUser("Sanjivani AI")

#positional arg (order matters here)
def descPet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name}.")
descPet("Dog", "Tommy")

'''
when u r definning function with default value,
while calling that fun it is not necessary to pass that arg:
'''
def descPet(pet_name,animal_type='Dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")
descPet(pet_name="Tommy")


#assignments
'''
1.
create program using maths & f strings and tell us how many days ,weeks , 
months we have left if we will live until 80 years
'''
print("Welcome to the Roller coaster")
height=int(input("Enter your Height:"))
age=int(input("Enter your age:"))

if(height>=120):
    print("Your Are Eligible to play roller Coster")
    if(12<age<=18):
        print("Ticket is ₹20")
    elif(age>18):
        print("Ticket is ₹50")
    elif(age==12 and height==120):
        print("Ticket is ₹10")
    elif(10<age<12):
        print("Ticket is ₹15")      
else:
    print("Sorry you are not allowed")

print("Welcome to roller coaster")
h=int(input("Enter your Height:"))
bill=0
if h>=120:
    print("You are eligible to play roller coster")
    a=int(input("Enter your Age:"))
    if a<12:
        print("Clid ticket are $5")
        bill=5
    elif a<=18:   
        print("Youth ticket are $7")
        bill=7
    else:
        print("Adult ticket  are $12")
        bill=12
    want_photo=input("Do you want photo Y OR N: ")    
    if want_photo=='Y':
        bill+=3
        print(f"your total bill will be {bill}")
    else:
        print(f"you total bill {bill}")
else:
    print("Sorry you are not allowed")

'''
2.
write program for roller coster if ur height is equal to or greather than 120cm
then ur elligible to play roller coster
if ur age is under 18 then ticket will be 20Rs
if ur greater then ticket will be 50Rs

add more condition

age is greater than 12 height 120 ticket 10Rs
and if ur bet 8-12 n height is 120 ticket 15Rs
'''

age=int(input("Enter age in years:"))
dayslive=age*365
monthslive=age*12
weekslive=age*52
totaldays=80*365
totalmonths=80*12
totalweeks=80*52
print(totalweeks)
print("totals days remain:",totaldays-dayslive)
print("totals months remain:",totalmonths-monthslive)
print("totals year remain:",80-age)
print("total weeks remain:",totalweeks-weekslive)

users=["Admin","Manager","Worker","Employee","Staff"]
for user in users:
    if user=="Admin":
        print("Hello admin")
    elif user=="Manager":
        print("Hello Manager")
    elif user=="Employee":
        print("Hello employee")
    elif user=="Worker":
        print("Hello worker")
    else:
        print("hello")
        
#password generator

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
 
#create new second  password
password=adjectives+nouns+str(number)+string.punctuation
print('Your new password is:%s' %password)
print('Welcome to password picker')
while True:
    nouns=random.choice(noun)
    adjectives=random.choice(adjective)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    #create new sec password
    password=adjectives+nouns+str(number)+string.punctuation
    print('Your new password is:%s' %password)
    response=input('would u like to generate another password? type y/n:')
    if response=='n':
        break

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
    
    
#total age prediction
print("What is ur age ")
years_today=input("Years:")
months_today=input("Months:")
days_today=input("days:")
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"your total age today in days {total_days_today}")
print("Let us assume u r expected to live 90 year")
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"ur remaining life in days {remaining_days_to_live}")

'''
write a program 
to calculate pizaa order bill
small 15
medium 20
large 25

if u want to add pepproni for small is add 2
if u want to add pepproni for medium n large  is add 3
if u want to add more cheez for any is add 1
'''

print("Welcome to pizza hut")
size=input("Enter size of pizza :")
bill=0
addpep=input("add pep y/n:")
addcheez=input("add cheese y/n:")
if size=="s":
    #print("Bill is 15")
    bill=15
    if addpep=="y":
     #   print("Bill is 17")
        bill=17
    if addcheez=="y":
      #  print("Bill is 16")
        bill=16
    if addpep=="y" and addcheez=="y":
       # print("Bill is 18")
        bill=18

elif size=="m":
    #print("Bill is 20")
    bill=20
    if addpep=="y":
     #   print("Bill is 20")
        bill=23
    if addcheez=="y":
      #  print("Bill is 23")
        bill=21
    if addpep=="y" and addcheez=="y":
       # print("Bill is 24")
        bill=24
elif size=="l":
    #print("Bill is 25")
    bill=25
    if addpep=="y":
       # print("Bill is 28")
        bill=28
    if addcheez=="y":
        #print("Bill is 26")
        bill=21
    if addpep=="y" and addcheez=="y":
        #print("Bill is 29 ")
        bill=29

print("Total bill amount is $",bill)
