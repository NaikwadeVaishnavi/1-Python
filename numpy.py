# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:27:50 2023

@author: vaish
"""

#Numpy
'''
numpy library is popular open sourcr python
used for scientific computing application
and it stands for Numerical Python
which consisting of multidimentional  array object and a 
collection of routines for processing the data

'''
#install numpy library
#go to base terminal
#pip install numpy
#conda install numpy
'''
while a python list contain different data type within a single list
all of element in a numpy array should be homogeneous
'''

#array in numpy
#create nDarray'
import numpy as np
arr=np.array([10,20,30])
print(arr)

#create a multidimentional array
arr=np.array([[10,20,30],[40,50,600]]) #-2Darray
print(arr)

'''
represent the minimum dimension
use ndmin param to specify how many minimum
dimension you wanted to created an array with minimum dimension
'''
arr=np.array([10,20,30,40],ndmin=3) #create 3D array
print(arr)

#change the data type
#dtype parameter 
arr=np.array([10,20,30],dtype=complex) #assign datatype =complex no
print(arr)

##get dimension of array
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(arr.ndim)
print(arr)

#find size of each item in array
arr=np.array([10,20,30])
print("Each item size in byte:",arr.itemsize)

#get shape & sizr of array
arr=np.array([[10,20,30,40],[60,70,80,90]])
print("Array size",arr.size)
print("shape",arr.shape)

#create a sequence of integer using arange()
arr=np.arrange(0,20,3)
print("a sequential array with step of 3:\n",arr)


#array indexing in numpy 
#a sequential array witn   step of 3

#[0 1 2 3 4 5 6 7 8 9 10]
#access a singlr element using index 
arr=np.array([0,1,2,3,4,5,6,7,8,9,10])
print(arr[2])#2
print(arr[-2])#9

#multi dimentional array indexing 
#access multi dimentional array element
#using array indexing
arr=np.array([[10,20,30,40,50],[20,30,50,10,20]])
print(arr)

print(arr.shape)#(2,5)
print(arr.size)#10
print(arr[1,1])#30
print(arr[0,4])#50

arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]#generating in step 2 
print(x) #[1 3 5 7]

#example
x=arr[-2:3:-1] #start from end but one(-2) upto 3 but not 3 in step  
print(x) #[8 7 6 5 4]


#indexing in numpy
multi_arr=np.array([[10,20,10,40],
              [40,50,70,90],
              [60,10,70,80],
              [30,90,40,30]])
print(multi_arr)

#slicing of array
#for multiple dimensional array NumPy arrays
#u can access the element as below

multi_arr[1,2] #to access the value qt row 1 and column 2 ==70
multi_arr[1,:]# row 1 and all col == array([40, 50, 70, 90])
multi_arr[:,1]# all row and 1 co l ==array([20, 50, 10, 90])

x=multi_arr[:3,::2] #col from 0 - 3 in all selected alternate col
print(x)
'''
[[10 10]
 [40 70]
 [60 70]]
'''

#integer array indexing = allow the selection of arbotatory items
#arange() = range function to array print num in given range of an array
#reshape(row),col == use to give shape to array
arr=np.arange(35).reshape(5,7)
print(arr)
'''[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]]
'''

#boolean array indexing
'''
advanced indexing occurs when an object 
is an array of boolean type 
such as may be returned from comparism operators
use this method when we want to pick element 
from the array which satisfy some condition
'''

arr=np.arange(12).reshape(3,4)
print(arr)

rows=np.array([False,True,True]) #0 th row only first and selected col
wanted_rows=arr[rows,:]
print(wanted_rows)
'''[[ 4  5  6  7]
 [ 8  9 10 11]]  here those rows have value true are got printed 
row with value false are not printed'''

#convert one dimentional array to list

#create
arr=np.array([10,20,30,40])
print(arr)
print(type(arr)) #<class 'numpy.ndarray'>
#convert
lst=arr.tolist()
print("List1 =",lst) 
print(type(lst)) #<class 'list'>

#convert multidimentional array to list 
arr=np.array([[1,2,3,4],
              [5,6,7,8],
              [6,4,2,1]])
print(arr)
lst=arr.tolist()
print(lst) #lsit of list
#[[1, 2, 3, 4], [5, 6, 7, 8], [6, 4, 2, 1]]

#convert list to array
'''list can convert into array by using buliding function

NumPy provide us with two function to use
when converting a list into array

1. numpy.array()
2. numpy.asarray()
'''

#create list
lst=[1,2,3,5]
#covert to array == numpy.array()
arr=np.array(lst)
print("Array :",arr) #Array : [1 2 3 5]
print(type(arr)) #<class 'numpy.ndarray'>


lst=[1,2,3,5]
#covert to array == numpy.asarray()
arr=np.asarray(lst)
print("Array :",arr) #Array : [1 2 3 5]
print(type(arr)) #<class 'numpy.ndarray'>

'''
numpy array properties
1 dtype
2 shape
3 size
4 arange
5 reshape
6 ndmin
'''

#shape
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape) #(2,3)


new_arr=arr.reshape(3,2)
print(new_arr)
print(new_arr.shape) # (3,2)


#operation using in numpy

#numpy operation  are divided into 3 main categories
'''
fourier transform and shape manipulation
mathematics and logical operation
linear algebra and random number generation
'''


#check version of numpy
import numpy as np
np.__version__

#numpy program to test whether none of the element of a given array is zero
z=np.array([1,2,3,4])
print("Original array : ",z)
print("Test if none of the element of the said array is zero")
print(np.all(z)) #check whether 0 value present or not if not return true

z=np.array([0,1,2,3])
print("Test if none of the element of the said array is zero")
print(np.all(z)) #if 0 value present return False

#numpy program to test whether none of the element of a given array is non-zero
x=np.array([1,0,0,0])
print("Original array ",x)
print("Test if none of the element of the said array is non-zero")
print(np.any(x)) #return true when any non zero value present

x=np.array([0,0,0,0])
print("Original array ",x)
print("Test if none of the element of the said array is non-zero")
print(np.any(x)) #return false when non zero not present

#test a given array element-wise  for finiteness (not infinity or not a number)
#infinity == np.inf && np.nan ==none
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print(a)
print("Test a given array element-wise for finiteness :")
#print true when finite num
print(np.isfinite(a)) #[ True  True False False] 


#numpy program program to test element wise for NaN of a given array
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print(a)
print("Test a given array element-wise for finiteness :")
#print true when nan
print(np.isnan(a)) #[False False  True False] 

'''
numpy program to create an element-wise comparison 
(greater,greater_equal,less,less_equal)
of 2 given array
'''
import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("Original arrays: ")
print(x)
print(y)

print("Comparison - greater") #[ True False]
print(np.greater(x,y))

print("Comparison -  greater equal") #[ True  True]
print(np.greater_equal(x,y))

print("comparison - less ") #[False False]
print(np.less(x,y))

print("Comparison - less equal")#[False False]
print(np.less_equal(x,y))

#numpy program to create 3x3  identity matrix
import numpy as np
array_2D=np.identity(3)
print("3x3 matrix :")
print(array_2D)

#numpy progrsm to generate random number between 0 and 1
import numpy as np
rand_num=np.random.normal(0,1,1)
print("Random no. between 0 and 1")
print(rand_num)

import numpy as np
rand_num=np.random.normal(0,1,2) #bet 0-1 2 num
print("Random no. between 0 and 1")
print(rand_num)

#write numpy program to create a 3x4 array and iterate over it
import numpy as np
a=np.arange(10,22).reshape((3,4))
print("Original array")
print(a)
print("Each element of the array is")
for i in np.nditer(a):
    print(i,end='')
    print()

#write a program to create a vector of length 10 with value
#evenly distribution between 5 and 50

import numpy as np
v=np.linspace(10,49,5) #10=start pt 49 end pt 5=total random vectors
print("length 10 with values evenly distribution between 10 - 49 ")
print(v)

#write numpy program to create 3x3 matrix 
#with values ranging from 2 to 10
import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)

#write numpy program to reverse an array (the first element become last )
import numpy as np
x=np.arange(12,38)  
print("Original array")
print(x)
print("Reversed array")
x=x[::-1]
print(x)

#numpy program to compute the (dot product) multiplication of two given matrix
import numpy as np
p=np.array([[1,0],[0,1]])
q=np.array([[1,2],[3,4]])
print("Original matrix")
print(p)
print(q)
result=np.dot(p,q) #.dot() for dot product
print("Result of said matrix multiplication")
print(result)


#numpy program to compute the  cross product of two given matrix
import numpy as np
p=np.array([[1,0],[0,1]])
q=np.array([[1,2],[3,4]])
print("Original matrix")
print(p)
print(q)
result1=np.cross(p,q)
print("cross product of the vector (p,q)")
print(result1)

result2=np.cross(q,p)
print("cross product of the vector (q,p)")
print(result1)

#numpy program to calculate determinant of square matrix
import numpy as np
from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print("Original 2D array")
print(a)
print("Determinant of matrix ")
print(np.linalg.det(a))

#numpy program to compute the eigenvalues and
#right eigen vectors of a given square matrix
 
import numpy as np
m=np.mat("3 -2;1 0")
print("Original array")
print("a\n",m)
w, v=np.linalg.eig(m)
print("Eigen value of given matrix",w)
print("Eigen vector of given matrix",v)

#compute inverse of matrix
import numpy as np
m=np.array([[1,2],[3,4]])
print("Original matrix")
print(m)
result=np.linalg.inv(m)
print("Inverse of matrix")
print(result)
