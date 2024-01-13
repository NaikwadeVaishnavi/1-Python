# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:15:25 2023

@author: vaish
"""

'''
PANDAS apply function to a column
below are quick examples
Using DataFrame.apply() to apply a function add column
'''
import pandas as pd
import numpy as np
data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
df

#ADD 3 to each element in column
def add_3(x):
    return x+3
df2=df.apply(add_3)
df2  

#add 3 to column A
df2=((df.A).apply(add_3))

#apply function to single column
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]

#apply to multiply columns
df[["A","B"]]=df[["A","B"]].apply(add_4)
df[["A","B"]]

'''
when u r going to apply function on multiple columns then u will have to pass
list of columns on which u have to operate
'''

#apply lambda function to each column

#lambda fun - anonymous function *syntax - (lambda arg : business logic)

df2=df.apply(lambda x:x+10)
df2

#apply() function on selected list of multiple columns
df[["A","B"]]=df[["A","B"]].apply(lambda x : x*10)
df[["A","B"]]


#transform() = instead of apply() we can use this method

def add_2(x):
    return x+2
df=df.transform(add_2)
df

#using pandas.Dataframe.map() to string column

df["A"]=df["A"].map(lambda A:A/2)
df

#using numpy function on single column
#using dataframe.apply() and [] operator

import pandas as pd
import numpy as np
data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
df

df["A"] =df["A"].apply(np.square)
df["A"]

df["A"]=np.square(df["A"])
df["A"]


import pandas as pd
import numpy as np 
technologies=({'Courses':["Spark","Pyspark","Hadoop","Python","Pandas","Hadoop",'Spark',"Python",None],
              'Fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
              'Duration':["30days","50days","55days","40days","60day ","35days","30days",'50days','40days'],
              'Discount':[1000,2300,1000,1200,2500,np.nan,1400,1600,0]
    })

df=pd.DataFrame(technologies)
df

df2=df.groupby(['Courses']).sum()
df2

df2=df.groupby(['Courses','Duration']).sum().reset_index()
df2


import pandas as pd
import numpy as np 
technologies=({'Courses':["Spark","Pyspark","Hadoop","Python","Pandas"],
              'Fee':[22000,25000,23000,24000,26000],
              'Duration':["30days","50days","55days",None,np.nan],
              'Discount':[1000,2300,1000,1200,2500]
    })

df=pd.DataFrame(technologies)
df
    
df.columns

#get the list of all columns names from headers
column_header=list(df.columns.values)
column_header

#pandas shuffle dataframe rows
#shuffle the dataframe rows & return all rows

#frac=1 100% shuffle of rows
df1=df.sample(frac=1)
df1

#frac=0.5 50%shuffle of rows
df1=df.sample(frac=0.5)
df1

#drop shuffle indexing from zero
#reset index after shuffling

df1=df.sample(frac=1).reset_index()
df1

#
df1=df.sample(frac=1).reset_index(drop=True)
df1

#join= used to join commom rows and columns

import pandas as pd
import numpy as np 
technologies1=({'Courses':["Spark","Pyspark","Python","Pandas"],
              'Fee':[22000,25000,23000,24000],
              'Duration':["30days","50days","55days",'40days'],
                 })


index_labels=['r1','r2','r3','r4'] 

df1=pd.DataFrame(technologies1,index=index_labels)
df1


import pandas as pd
import numpy as np 
technologies2=({
    'Courses':['Spark',"java",'Python','go'],
    'Discount':[2000,2300,1200,2000]
    })

index_labels2=['r1','r6','r3','r5']

df2=pd.DataFrame(technologies2,index=index_labels2)
df2

'''
pandas inner join is mostly used join it is used to join two dataframe on indexes
when indexex dont match the rows get dropped from both dataframe
pandas join   by default it will join table row get dropped from both dataframe
'''
#pandas join   by default it will join table row get dropped from both dataframe
df3=df1.join(df2,lsuffix='_left',rsuffix="_right")
df3

#inner join  
df3=df1.join(df2,lsuffix='_left',rsuffix='_right',how='inner')
df3

#pandas left join dataframe
df3=df1.join(df2,lsuffix='_left',rsuffix='right',how='left')
df3

#pandas right join dataframe
df3=df1.join(df2,lsuffix='_left',rsuffix='right',how='right')
df3

#pandas INNER join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='inner')
df3

#pandas LEFT join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='left')
df3

#pandas RIGHT join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='right')
df3

#pandas.merge == inner join
df3=pd.merge(df1,df2)
df3

#using DataFrame.merge()
df3=df1.merge(df2)

#use pandas.concat() = to concat 2 dataframe
import pandas as pd
df1=pd.DataFrame({
      'Courses':['Spark',"Pyspark","Python","Pandas"],
      'Fee':[20000,25000,22000,24000]
      })

df2=pd.DataFrame({
      'Courses':['Pandas',"Hadoop","Hyperian","Java"],
      'Fee':[25000,25200,24500,24900]
      })

data = [df1,df2]

df3=pd.concat(data)
df3

