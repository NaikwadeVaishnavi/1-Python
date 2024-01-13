# -*- coding: utf-8 -*-
'''
Created on Fri Jul 21 08:15:37 2023
@author: vaish
'''

print("Hello World!")
x=1
print(x)
print(type(x))
x=1.0
print(type(x))



age1=input("plz Enter your age:")
print(type(age1))
print(age1)

age2=input("plz Enter your age:")
print(type(age2))
print(age2)

age=age1+age2                         #here concatenation is done
print(age)


#type casting 
age1=int(input("plz Enter your age:"))
print(type(age1))
print(age1)

age2=int(input("plz Enter your age:"))
print(type(age2))
print(age2)

age=age1+age2                           #here addition is done
print(age)


#floating pt numbers

x=10                                 #i/p in form of str
print(type(x))
print(float(x))
y=float(x)                           #type casting 
print(y)
print(type(y))

#converting to floats
#as with int it is possible to convert other
#types such as an int or a string a float

int_value =100
string_value = '1.5'
float_value=float(int_value)
print('int value as a float:', float_value)
print(type(float_value))
float_value=float(string_value)
print('string value as a float:', float_value)
print(type(float_value))


#complex numbers

c1=1                        #real no.
c2=2j                       #imaginary no.
print("c1:",c1," c2:",c2)
print(type(c1))
print(type(c2))


#boolean values

#python supports another type called boolean
#a boolean type can only be one value "True" or "False"
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)

#we can also convert string format int Boolean 
#as long as string contain value either True or False(nothing else)

status=bool(input("Ok it is confirmed? :"))
print(status)
print(type(status))


#if u r performing any arithmatic operation(+,-,*) on integer then resultant is also integer

h=10
a=15
print(h+a)
print(type(h+a))
print(10*4)
goals_for=10
goals_against=7
print(goals_for-goals_against)
print(type(goals_for-goals_against))

#division of 2 int no is float

a=12
b=4
print(a//b)   #give int output
print(a/b)    #gives float output

#modulus operator(to find remainder)
print(a%b)
print(b%a)


#power operator(**)

a=5
b=3
print(a**b)


#assignment operator / compound operator

x=0
x+=1                #behave as x=x+1
print(x)


# None value

winner=None

print('winner:', winner)
print('winner is None:', winner is None) 
print('winner is not None:', winner is not None)
print(type(winner))
print('Set winner to True') 
winner = True


#flow of control If Statements

num=int(input("Enter num :"))
if num<0:
    print(num)
else:
    print("Number is negative")

