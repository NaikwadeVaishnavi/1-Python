# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:08:59 2023

@author: vaish
"""

#dataframe =table
#single col known as series
import pandas as pd
songs2=pd.Series([145,142,38,13],name='counts')
#it is easy to insept the index of series (or data )
songs2.index
'''
the index can be string based as well in which case pandas indicates 
that the datatype for the index is object (not string)
'''
songs3=pd.Series([145,142,38,13],name='counts',index=['Paul','John','George','Ringo'])
songs3.index
songs3

#The NaN value =
'''
NaN, standing for not a number, is a numeric data type 
used to represent any value that is undefined or unpresentable.
'''

'''
this value stands for NaN A Number 
and is usually ignored in arithmetic 
operations (similar to NULL IN SQL)
if u load data from CSV file
an empty value for an otherwise
'''

#numeric column will become NULL

import pandas as pd
#read csv file read_csv *CSV (comma separator value file)
f1=pd.read_csv("C:/1-python/age.csv.xls")

#here we have importes age.csv file so we used 'read_csv' here
#in file age of ghansham is not mension so it will print 'nan' in age cell 

f1

import pandas as pd
#read excel file read_excel
df=pd.read_excel("C:/1-python/Bahaman.xlsx")

df

#Numpy
import numpy as np
numpy_ser=np.array([145,142,38,13])
songs3[1]
#142
numpy_ser[1]
#they both have common method
songs3.mean()
numpy_ser.mean()

'''
the PANDAS SERIES DATA STRUCTURE provides a support for the basic CRUD operation
create read update delete 
'''

#CREATION of series
george=pd.Series([10,7,1,22],
                 index=['1968','1967','1970','1970'],
                 name='George Songs')
george

'''
the previous example illustarte 
an interesting features of pandas  - 
the index value strings and they are not unique this cam cause 
some confusion but can also be useful 
when duplicate index items are needed
'''
#to read or select the data from a series
george['1968']

#in below case it will gives 2 output as there are 2 entry of 1970
george['1970']



#UPDATE the value in series
'''
updating values in series can be a little tricky as well
to update a value 
for a given index label
the standard index assignment operation
'''
george['1969']=68
george['1969']



#DELETION in series - if we not mension name it will take 0 by default
#del statement appears to have problem with duplicate index

s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

#CONVERT TYPES
'''
string use.astype(str)
numeric  use pd.to_numeric
integer use .astype(int)
*Note : this will fail with NaN
datetime used pd.to_datetime
'''
import pandas as pd
songs_66=pd.Series([3,None,11,9],
                   index=["George","Ringo","John","Paul"],
                   name='Counts')
songs_66.dtypes ##dtype('float64') is output

pd.to_numeric(songs_66.apply(str)) 
#above line  will display ValueError as series contain None value

pd.to_numeric(songs_66.astype(str),errors='coerce')
#it we pass errors='coerce' used to ignore error bt datatype is not changed
#we can see that it supports many format

songs_66.dtypes

#Dealing with None value
#The .fillna method will replace the none value with given value

songs_66.fillna(-1)


#NaN value can be drop from the series
#the series using .dropna -  row will get deleted which contain None value

songs_66.dropna()                   

#Append combining and joining two series

songs_69=pd.Series([7,16,21,39],
                   index=['Ram','Sham','Ghansham','Krishna'],
                   name='Counts')
#to concatenate 2 series together simply use the .append
#after appending it will get print vertically instead of horizontally

songs=songs_66.append(songs_69)
songs



#matplotlib= module pyplot=submodule

import matplotlib.pyplot as plt
fig=plt.figure()
 #plt.figure() = create a figure object.
songs_69.plot() 
#.plot=draws a line from point to point.
plt.legend()
#.legenda =

fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

#histogram

import numpy as np
data=pd.Series(np.random.randn(500),name='500 random number')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

#check version of pandas
#upgrade pandas = pip install --upgrade pandas

#check version of python

import pandas as pd 
pd.__version__

