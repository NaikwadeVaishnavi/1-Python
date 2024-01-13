# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:05:38 2023

@author: vaish
"""

#program to create and display series a one-dimentional array-like
#containing an array of data
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)

'''
program to convert a panda module series 
to python list and its type
'''
print(type(ds))

print("Convert pandas Series to python list")
print(ds.tolist())
print(type(ds.tolist()))

#program to add,sub,multiply
'''
sample series [2,4,6,8,10]
              [1,3,5,7,9]

'''
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds=ds1+ds2
print("Add two Series")
print(ds)
ds=ds1-ds2
print("Subtract two Series")
print(ds)
ds=ds1*ds2
print("Multiply two Series")
print(ds)
ds=ds1/ds2
print("Divide two Series",ds)
print(ds)
#program to compare series
'''sample series [2,4,6,8,10]
              [1,3,5,7,9]
'''
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare Series")
print("Equals")
print(ds1==ds2)
print("Greater Than")
print(ds1>ds2)
print("Less Than")
print(ds1<ds2)

#program to convert dictionary to pandas series
'''
original dict:{
    'a':100,'b':200,'c':300,'d':400,'e':800}
'''
import pandas as pd
d1={'a':100,'b':200,'c':300,'d':400,'e':800}
print("Original Dict")
print(d1)
new_series=pd.Series
print("Converted Series")
print(new_series)

#program to convert numpy array to pandas series
import numpy as np
import pandas as pd
n_a=np.array([10,20,30,40,50])
print("Numpy array")
print(n_a)
new_series=pd.Series(n_a)
print("coverted pandas series")
print(new_series)

#program to change data type of given column or a series
'''
sample series
Original data series
0       100
1       200
2       python
3       300.12
4       400
dtype:object
Converted data series
0       100.00
1       200.00
2       NaN
3       300.12
4       400.00
dtype:float64
'''
import pandas as pd
s1=pd.Series(['100','200','python','300.12','400'])
print("Original Series")
print(s1)
print("Change the said data type to numeric")
s2=pd.to_numeric(s1,errors='coerce')
print(s2)

#program to convert the first column of a dataframe as a series
'''
[:,:] == all rows all cols
iloc[:] ==start of row : end of row i.e line of control
integer-location based indexing for selection by position.
one of the functions defined in the Pandas module 
that helps us to select a specific row or column 
from the data set. 
'''
import pandas as pd
d={
   'col1':[1,2,3,4,7,11],
   'col2':[4,5,6,9,5,0],
   'col3':[7,5,8,12,1,11]
   }
df=pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
s1=df.iloc[:0] #s1=all rows and 0th column 
print("1st column as a Series")
print(s1)
print(type(s1))


#assign index to each elements in column of series
'''
in general column index has not index cause it hase overall column 
index 
to assign index to each item in column this following function is used 
stack() used to convert coulumn into index'''
import pandas as pd
s=pd.Series([
            ['Red',"Green","White"],
            ["Red","Black"],
            ["Yellow"]
            ])
print("Original Series")
print(s)
s=s.apply(pd.Series).stack().reset_index(drop=True)
'''#alternamte way to above line 
s1=s.apply(pd.Series)
s2=s1.stack()
s3=s2.reset_index(drop=True)
print(s3)
'''
print("One Series")
print(s)

'''
DataFrame -stack()
the stack() function is used to stack list
prescribed levels(s) from columns to index
return  a reshaped DataFrame or Series
having a  
'''

#panda program to add some data in existing series
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("Original Series")
print(s)
print("\nData series after adding some data: ")
new_s=pd.concat([s,pd.Series([500,"php"])],ignore_index=True)
print(new_s)

#write a panda program to change the order of index of given series
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("Original  Data Series")
print(s)
new_s=pd.Series(s).sort_values()
print(new_s)

#write a panda program to change the order of index of given series
'''
sample output
A    1
B    2
C    3
D    4
E    5
dtype:int64
Data series after changing the order of index
B    2
A    1
C    3
D    4
E    5
dtype:int64
'''
import pandas as pd
s=pd.Series(data=[1,2,3,4,5],index=['A','B','C','D','E'])
print("Original Data Series:")
print(s)
s=s.reindex(index=['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s)
