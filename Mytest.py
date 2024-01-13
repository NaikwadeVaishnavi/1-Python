# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:55:25 2023

@author: vaish
"""

#1 program to check if list is empty
def check(lst):
    if (len(lst)==0):
        return True
    else:
        return False
lst=[]
check(lst)

#2 lst comph construct a lst frm square 
#of each element in lst

lst=[x for x in range(0,5)]
print(lst)
lst2=[x*x for x in lst]
print(lst2)

#3 check if given key is already present in dict 
dict1={
       'A':"Apple",
       "B":"Ball",
       'C':"Cat"
       }

key_to_check = 'b'

if key_to_check in dict1:
    print("key is present")
else:
    print("Key is not present")


#4 create range 100-160  with step of 10 sec 
#using dict comprehenssion where each num in range is key  and
#each item divided by 100 is value

result_dict = {num:num/100 for num in range(100,161,10)}
print(result_dict)


#5 dataframe course, fee duration abd add tutor column

import pandas as pd
data={
      'Courses':['Data Science','ML',"AI","Python"],
      'Fee':[1000,2000,3000,4000],
      'Duration':['31day','21day','11day','41day']
      }
df=pd.DataFrame(data)
df
df['Tutor'] = ['Vaishnavi','Vedika','Vasudha','Nikita']
print(df)

#6 u have already created dataframe write it to csv
df.to_csv('courses.csv')
print("DataFrame written to 'courses.csv'")


#7 python function to which return multiple value



#8 function take 2 arg a and b return multiplication 
def mul(a,b):
    return a*b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("Multiplication of a and b is :",mul(a,b))

product = lambda a, b : a * b
print(product(a,b))

#9 numpy program to test if any of the element of 
#given array is non-zero 
import numpy as np
array=np.array([1,2,3,4,0])
print(np.any(array))

#10 display bar chart of the popularity og programming lang
#lang:java,python,php,javascript,c#,c++
#rating 5,9.5,7,8.5,6.7,7.5
import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C']
popularity = [5,9.5,7,8.5,6.7,7.5] 
plt.bar(languages, popularity)
plt.show()
