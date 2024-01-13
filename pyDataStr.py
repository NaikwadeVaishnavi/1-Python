# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:36:12 2023

@author: vaish
"""
#tuple & list
#tuple() collection of object which is ordered immutable(unchangeble) 
'''
used to store multiple items items in single variable
collection of object which is ordered immutable(unchangeble) 
tuple can hold different data type
'''
#creating tuple
tup1=(1,3,5,7)
#accessing tuple element 
print(f"tup1[0] :\t{tup1[0]}")
print("tup1[1] :\t",tup1[1])
print("tup1[2] :\t",tup1[2])
print("tup1[3] :\t",tup1[3])

tup2=(1,"strings",1.2)
print(f"tup2[0] :\t{tup2[0]}")
print("tup2[1] :\t",tup2[1])
print("tup2[2] :\t",tup2[2])

#iterating over tuple
tup3=("Apple","Banana","Orange","Plum")
for i in tup3:
    print(i)

#tuple related function
#len()-return length of tuple
print(len(tup3))

#count()-return occurance of specific item in tuple 
print(tup3.count("Apple"))

#index()- return the address of item
print(tup3.index("Apple"))

#check element exist in tuple
if "Orange" in tup3:
    print("Yes it is in tuple")

#nested tuple tuple inside tuple
tup4=(tup1,tup2,tup3)
print(tup4)

#allow duplicate
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# list[] mutable index ordered 
list1=["car","bike","cycle","aeroplane",1]
#access element
for i in list1:
    print(i)
#length
print(len(list1))
#count occurance
print(list1.count("car"))
#nested list
lst2=[1,2,3]
lst3=[12,24,list1,67,"sai",lst2]
print(lst3)
#access last index value
print(list1[-1]) 

lst1=['jhon','pual','ram','sham']
print(lst1[-1])
lst1[0],lst1[-2]

print("Element in range 2-4",lst1[2:4])
print("Reversed lst1 :",lst1[::-1])
print("list ",lst1[0:])

#append 
lst1=['jhon','pual','ram','sham']
lst1.append("sai")
print(lst1)

#extend
lst1.extend(["Albert","Bobby"])
print(lst1)

#insert 
a_list=["Adele","Madomma","Cher"]
print(a_list)
#inserted at given index 
#here we have given index 1 so it will b inserted at 1 index
a_list.insert(1,"Paloma")
print(a_list)

#list concatenation
lst1=[1,2,3,4]
lst2=["a","b","c"]
lst3=lst1+lst2
print(lst3)

'''
assignments
1
take 5 num in list n find min and max of list

2
take 5 string in list make it reverse
3
take 10 num in list write script to search for a value
4
take 10 num in list insert duplicate num write script to find duplicates
5
take vowel letters n non vowels letter in list find total no of vowels in list

'''
#take 5 num in list n find min and max of list
lst=[1,20,3,4,10]
print(max(lst))
print(min(lst))

#take 5 string in list make it reverse
lst1=["tiger","monkey","elephant","snake"]
print(lst1[-1])

#take 10 num in list write script to search for a value
lst2=[11,12,13,14,15,16,17,18,19,20]
print(lst2.index(20))

#take 10 num in list insert duplicate num write script to find duplicates
lst3=[21,22,23,22,25,26,27,28,29]
print(lst3.append(22))
print(lst3)
print(lst3.index(22))

#take vowel list n non vowels letter in list find total no of vowels in list
lst4=["a","b","c","d","e","f","g","h","i","j","a","e","i","o","u","k","l","m","n","o","p",
      "q","r","s","t","u","a","e","i","o","u","v","w","x","y","z"]
print("occurance of a",lst4.count("a"))
print("occurance of e",lst4.count("e"))
print("occurance of i",lst4.count("i")) 
print("occurance of o",lst4.count("o"))
print("occurance of u",lst4.count("u"))

#take 5 numbers in list and find minimum and  maximum of list
lst=[81,43,56,78,21]
print(min(lst))
print(max(lst))



#take 5 numbers in list and make it reverse
lst=[1,2,3,4,5]
lst1=lst[: : -1]
print(lst1)


#take 10 number in the list write script to search for value
lst=[1,2,3,4,5,6,7,8,9,10]
num=int(input("Enter Number you want to search:"))
for i in lst:
   if(num==i):
       print(num,"is present in list ")
       break
else:
     print("Number not found")


#take 10 number in the list insert some duplicate number write script to find duplicates
lst1=[1,2,3,4,5,6,7,8,9,10,9,6]
lst2=set(lst1)
duplicate=len(lst1)-len(lst2)
print(duplicate,"values are duplicate in list")


#take vowels in list and non vowels letter find total num of vowels in list
lst=["a","s","v","e","i","k","o","m","u","o"]
count=0
for i in lst:
    if (i=="a") or (i=="e") or (i=="i") or (i=="o") or(i=="u"):
        count=count+1
else:
    print(count)


#remove()- remove particular data from list 
another_list=["gary","mark","robbie","jason","howard"]
print(another_list)
another_list.remove("robbie")
print(another_list)

#pop() remove element from list
'''
pop()
two methods:
    it takes an index which is the index of the item to remove from  than the '
    object itself  
'''
lst6=['once','upon','a','time']
print(lst6)
print(lst6.pop(2))
print(lst6)

#insert into list
lst6=['once','upon','a','time']
print(lst6.insert(4,"there"))
print(lst6)

#set{} ==dont allow duplicate element 
basket={"Apple","Banana","Orange","Plum","Apple"}
print(basket)

#accessing element
for item in basket:
    print(item)

#add()= Adding items to set
basket={"Apple","Banana","Orange"}
basket.add("plum")
print(basket)



#update() =add one n more element then use update() n u have to pass list
basket={"Apple","Banana","Orange"}
basket.update(["Pineapple","Coconut","pear"])
print(basket)

#length of set
basket1={12,35,57,86}
print(len(basket1))
print(max(basket1))
print(min(basket1))

#remove element from set
basket={'Orange', 'Banana', 'Coconut', 'Pineapple', 'Apple', 'pear'}
basket.remove("Pineapple")
print(basket)

#set operation
s1={'Orange', 'Banana', 'Coconut', 'Pineapple'}
s2={"Strawberry","Plum","pear","lime","Coconut"}
print("Union:",s1 | s2) #union symbol== "|"
print("Intersection:",s1&s2) #intersection symbol == "&"
print("Difference :",s1-s2) 

#dictonary{"key":"value"} set association between key & value, unorders, mutable, indexed
capitals={"Maharashtra":"Mumbai",
          "Gujarat":"Ahmadabad",
          "UP":"Lakhnow",
          "Karnataka":"Banglore",
          "Andrapradesh":"Hydrabad"
          }
print(capitals)
print(capitals.keys())
print(capitals.values())
print("Capitals[Maharashtra]:",capitals['Maharashtra'])
#adding new entry take key in form of the list
capitals["West Bengal"]="Kolkatta"
print(capitals)

#changing key value
capitals["Gujarat"]="Gandhinagar"
print(capitals)

#removing an entry
capitals.pop("Karnataka")
print(capitals)

#delete element
del capitals['UP']
print(capitals)

#accessing keys
for states in capitals:
    print(states)
    
#access values
for states in capitals:
    #print(states,end=",") #get keys
    print(capitals[states]) #get values
    
#values,keys and items here we will get tuple as o/p
print(capitals.keys())
print(capitals.values())
print(capitals.items())

#check membership
print("Karnataka " in capitals)
print("Bihar"  not in capitals)

#obtain the length
print(len(capitals))

#dict have value in tuple
seasons={"Summer":("Feb","Mar","Apr","May"),
         "Rainy":("Jun","Jul","Aug","Sept"),
         "Winter":("Oct","Nov","Dec","Jan")}
print(seasons["Rainy"]) #print tuple  of rainy season months
print(seasons["Rainy"][0])#print rainy season first months

#dict methods
print(capitals)
print(capitals.get("Maharashtra"))

#dict dont allow duplicates
#dict dont have same items with same value it will print last updated value
dict2={
      "Brand":"Maruti",
      "Model":"Breeza",
      "Year":2021,
       "Year":2022
       }
print(dict2)

#loop through dict it will show only keys
for x in dict2 :
    print(x) #print keys
    print(dict2[x]) #it will print value

