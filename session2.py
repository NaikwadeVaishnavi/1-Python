# -*- coding: utf-8 -*-
'''
Created on Mon Jul 24 08:57:06 2023

@author: vaish
'''

#elif statement

saving =float(input("Enter savings: "))
if saving==0:
    print("Sorry u dont have savings")
elif saving<500:
    print("Well done!")
elif saving<1000:
    print("Thats a tidy sum")
elif saving<1000:
    print("Welcome sir!")
else:
    print("ok,Thank you!")

#while loop - conditional statement

count=1
print("Starting")
while(count<=10):
    print(count)
    count+=1
print("End")

#for loop

print("print values on range")
#last digit is excluded as for loop excuted for n-1 range
for i in range(2,10):
    print(i)
    print("Done")

#break statement - it will break the loop from breakpoint and stop the execution of loop

num=int(input("Enter num:"))
for i in range(0,16):
    if i==num:
        break
    print(i)
print("Done")

#anonymous variable(_)

for _ in range(0,10):
    print(".",end='') 
    print()
#if u want to output horizontally then u can use "end"
for _ in range(0,10):
    print(".",end='')

#break loop statements'

print("Only if all the iterations completed")
num=int(input("Enter num:"))
for i in range(0,6):
    if i==num:
        break
    print(i," ",end=' ')
    print("Done")

#location of print changed
num=int(input("Enter num:"))
for i in range(0,6):
    if i==num:
        break
    print(i," ",end='')
print("Done")  

#print odd num in range

start,end=4,19
for i in range(start,end+1):
               if i%2!=0:
                   print(i,end=" ")

#print even num in range

start,end=4,19
for i in range(start,end+1):
               if i%2==0:
                   print(i,end=" ")                  

#print even num using range fun range(start,end,interval)

for i in range(4,15,2):
    print(i,end=' ')
print()
#print odd num using range fun 
for i in range(3,15,2):
    print(i,end=' ')
print()


#print even
x=int(input("Enter start range: "))
y=int(input("Enter end range: "))
for i in range(x,y):
    if i%2==0:
        print(i,end=" ")

#prime no. in range

x=int(input("Enter num: "))
for i in range(2,x):
    if (x%i==0) :
        print("not a prime number")
        break
    else:
        print("is a prime number")
        break

#palimdrome

s=input("Enter input:")
t=''
for i in s:
    t=i+t
if s==t:
    print("yes it is palimdrome")
else:
    print("No it is not palimdrome")

#leap year

x=int(input("Enter year:"))
if x%4==0 or x%100!=0 or x%400==0:
    print("leap year")
else:
    print("Not a leap year")

#Mario pyramid

#square block
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()


#right half pyramid
for i in range(5):
    for j in range (i+1):
        print("#",end=' ')
    print()

#inverted right pyramid

for i in range(5):
    for j in range (5-i):
        print("#",end=' ')
    print()

x='awesome'      #global variable
def my_fun():
    print("Python is "+x)
my_fun()
x='awesome'
def my_fun():
    x='fantastic'        #local variable
    print("Python is "+x)
my_fun()
print("Python is "+x)

#dictonary

x={"name":"Vaishnavi","age":"21"}
print(type(x))

x='this is python it is powerfull'
print(x)

#string slicing
x='python'
print(x[2:6]) #print between index 2-6 bt exclude index 2
print(x[ :3]) #slicing from start
print(x[3:])  #slicing from end
print(x[::-1]) #reverse print
print(x[-5:-2]) #slicing from end point of string


#uppercase
x="sAI"
print(x.upper())
print(x.lower())

#remove white space "strip"
x="This is python"
print(x.strip())

#replace
x="hello world"
print(x.replace("world","vasudha"))

#split
x="hello, world"
 #seperator is comma
print(x.split(",")) #after spliting in output we will get list

x="hello world"
print(x.split(" ")) #seperator is space

#slicing reverse
x="hello world"
print(x[::-1]) #reverse print

x="hello world"
print(x[::-2]) #skip 1 letter during slicing

#find location of any value
x="This is python"
print(x.find("is")) #return index of value

x="hello"
y="world"
print(x+y)
print(x+" "+y) #white is added


#u cannot concate string with int u have to concat the int to str
x=36
y="my name is anthony"
#print(x+y) this is invalllid
#u can use f string i.e number manupulation using fstring
print(f"my name is anthony and my age is {x}") 

quantity=3
item_no=54
price=67
print(f"I wany {quantity} pieces and item number is {item_no}, its price is{price}")

my_order="I wany {} pieces and item number is {}, its price is{}"
print(my_order.format(quantity,item_no,price))

my_order="I wany {0} pieces and item number is {1}, its price is{2}"
print(my_order.format(quantity,item_no,price))

#print "" in string \"---\"(escape char) it will not allow "" inside "" 

x="This is python,\"It is interesting\""
print(x)

