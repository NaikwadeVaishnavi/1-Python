# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:33:23 2023

@author: vaish
"""

#add all items in list

def sumLst(sumLst):
    sum=0
    for i in sumLst:
        sum=sum+i
    return(sum)
print(sumLst([24,26]))

#multilpy all item

def mulLst(mulLst):
    mul=1
    for i in mulLst:
        mul=mul*i  #mul*=i
    return(mul)
print(mulLst([24,0]))

#largest num in list
lst=[12,13,2453,765]
print(max(lst))
print(min(lst))

''' 
count no of string which satisfy condition that str len is 2 or more and 
first and last char is same
'''
lst=['abc','xyz','aba','1221']
count=0
for i in lst:
    if len(i)>=2:
        if i[0]==i[-1]:
            count+=1 
print(count)


'''
program to get a list sorted in increasing order by last element in  each tuple 
from a given list of non empty tuple
ip =[(2,5),(1,2),(4,4),(2,3),(2,1)]
op =[(2,1),(1,2),(2,3),(4,4),(2,5)]
'''
#print(ip[1])
def last(n):
    return n[-1]
def sort_list(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list([(2,5),(1,2),(4,4),(2,3),(2,1)]))

#remove duplicate from a list
lst=[10,20,30,20,10,50,60,40,80,50,40]
dup_item=set(lst)
uniq_item=[]
def removeduplicate():
    for i in lst:
        if i not in uniq_item:
            uniq_item.append(i)
            
removeduplicate()
print("Unique item",uniq_item)

#alternate
lst1=[10,20,30,20,10,50,60,40,80,50,40]
st1=set(lst1)
#since set remove duplicate hence list convert to set
print(st1)
lst2=list(st1)
print("Unique item",lst2) 


#copy a list
original_list=[1,2,3]
new_list=list(original_list)
print("original_list",original_list)
print("new copied list",new_list)


'''
find list of words that are longer than n(here 3) from 
a given list of word
'''
def longWord(n,str):
    word_len=[]
    txt=str.split(" ")
    for x in txt:
        if len(x)>n:
            word_len.append(x)
    return word_len
print(longWord(3, "The quick brown fox jumps over the lazy dog"))

#take 2 list as input n return comman members from the list


def commonItem(lst1,lst2):
    for a in lst1:
        for b in lst2:
            if a==b: 
                result=True
                return result
print(commonItem([1,2,3,5,6],[5,6,7,8,9,10]))

#calulate diff bet 2 list
lst1=[1,3,5,7,9]
lst2=[1,2,4,6,7,8]
s1=set(lst1)
s2=set(lst2)
lst3=list(s1-s2)
print("List 1 - list 2",lst3)
lst4=list(s2-s1)
print("List 2 - list 1",lst4)
print("total unique",lst3+lst4)

#convert list of char into string
#join() used to join the char
lst=["a","b","c","d"]
str1=''.join(lst)
print(str1)

#find index of item in list
num=[12,324,56,23,67,12,75,12,45,897]
print(num.index(23))

#concat list or append one list to other list
lst1=[1,3,5,7,9]
lst2=[1,2,4,6,7,8]
lst3=lst1+lst2
print(lst3)

a='z'
print(type(a))



