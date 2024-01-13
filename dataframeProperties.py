
#create using constructor
#create pandas DataFrame from List
'''since we have not given name and index the dataframe
 by default assign the incremental sequence number as labels to both
rows and column these are called index 
 '''
import pandas as pd 
technologies=[ ["Spark",20000, "30days"],
              ["Pandas",20000, "40days"]
              ]
df=pd.DataFrame(technologies)
print(df)

#Add column and rows label to the DataFrame
column_name=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_name,index=row_label)
print(df)

# dtypes == to check datatypes 
df.dtypes

#u can also assign custom data type to column
#set custom type to DataFrame

import pandas as pd
technologies={'Courses':["Spark","HAdoop","Python","pandas","oracle","java",'pyspark'],
              'Fee':["20000","25000","26000","22000","24000","21000","22000"],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

#convert all types to best possible types
#here all object datatype converted into string type 

df2=df.convert_dtypes()
print(df2.dtypes)

#change all column to same type 
#cinvert string datatype to object

df=df.astype(str)
print(df.dtypes)

#change type for one or multiple columns
#here we are assigning specific data types

df=df.astype({"Fee":int ,"Discount":float})
print(df.dtypes)

#convert data types for all columns in a list
df=pd.DataFrame(technologies)
df.dtypes
cols=["Fee","Discount"]
df[cols]=df[cols].astype('float')
df.dtypes

#ignore error
df=df.astype({"Courses":int},errors='ignore')
df.dtypes

#generate / raise error
df=df.astype({"Courses":int},errors='raise')
df.dtypes

#convert feed column to numeric type
df=df.astype(str)
print(df.dtypes)


import pandas as pd
technologies={'Courses':["Spark","HAdoop","Python","pandas",None,"java",'pyspark'],
              'Fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days"," ","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df=pd.DataFrame(technologies)
df

#Convert dataframe to csv 
df.to_csv('data_file.csv')
#data_file.csv will get created in 1-python folder

row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
df
#DataFrame properties
df.shape 
#(7,4)
df.size 
#28
df.columns 
#Index(['Courses', 'Fee', 'Duration', 'Discount'], dtype='object')
df.columns.values
#Index(['Courses', 'Fee', 'Duration', 'Discount'], dtype='object')
df.index 
#RangeIndex(start=0, stop=7, step=1)
df.dtypes

#accessing one columns
df['Fee']
#accessing two columns content
df[['Fee','Duration']]
#select certain rows and assign it to another dataframe
df2=df[6:]
df2
#access certain cell from column  'duration'
df['Duration'][3]
#subtracting specific value from a column
df['Fee']=df['Fee']-500
df['Fee']

#pandas to manipulate dataframe 
#describe  dataframe for all numeric columns
df.describe()
#it will show 5 number summary

df=pd.DataFrame(technologies,index=row_labels)

#assign new header by setting new column names 
df.columns=['A','B','C','D']
df

#rename column names using rename() method
#rename() - rename pandas Dataframe columns
'''
need of rename()= sometime we found space in name n it will not allowed 
so to rename it is used
'''
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df
'''
when accessing rows use axis=1 and 
when accessing column use axis='columns'
'''
df #origianl dataframe
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2
df2=df.rename(columns={'A':'c1','B':'c2'})
df2

#drop()-used to delete the rows and columns of given range
#Drop DataFrame Rows and columns
df=pd.DataFrame(technologies,index=row_labels)

#drop rows by labels
df1=df.drop(['r1','r2'])
df1

#delete rows by position/index
df1=df.drop(df.index[1:3])
df1

#delete rows by index range
df1=df.drop(df.index[2:])
df1

#when u have default indexex for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1

df=pd.DataFrame(technologies)
df1=df.drop([0,3]) #it will remove row0 and row3
df1

#drop rows and columns in specific range
df=pd.DataFrame(technologies)
df1=df.drop(range(0,2)) #it will delete 0 and 1
df1


# Drop column by index
print(df.drop(df.columns[1], axis=1))
df=pd.DataFrame(technologies)

# using implace=True
df.drop(df.columns[2], axis=1, inplace=True)
print(df)
########################################################
df=pd.drop(["Courses", "Fee"], axis=1)
print(df)

#df=pd.DataFrame(technologies)


##################################
#axis=1..operation on column
#axix=0..operation on row
#Drop column from list of column
df=pd.DataFrame(technologies)
df.columns
liscol=["Courses","Fee"]
df2=df.drop(liscol,axis=1)
df2

#dropping of column 
import pandas as pd
technologies=({'Courses':["Spark","HAdoop","Python","pandas",None,"java",'pyspark'],
              'Fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days"," ","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    })
df=pd.DataFrame(technologies)
print(df)
#drop column by name

#drop 'Fees' column
df2=df.drop(["Fee"],axis=1)
print(df2)

#explicitely using parameter name label
df2=df.drop(labels=['Fee'],axis=1)
df2

#alternately u can also use columns instead of labels 
df=pd.DataFrame(technologies)

#using inplace=True
df.drop(df.columns[2],axis=1,inplace=True)
df


df2=df.drop(df.columns[1],axis=1)
df2

#drop two  or more columns  by label name 
df=pd.DataFrame(technologies)
df2=df.drop(["Courses","Fee"],axis=1)
df2

#drop two  or more columns  by index
df=pd.DataFrame(technologies)
df
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)

#drop columns from list of columns
df=pd.DataFrame(technologies)
df
lisCol=["Courses","Fee"]
df2=df.drop(lisCol,axis=1)
df2

#remove columns from DataFrame inplace
df=pd.DataFrame(technologies)
df
df.drop(df.columns[1],axis=1,inplace=True)
df

#pandas select rows by index(position/label) use iloc
import pandas as pd
import numpy as np 
technologies=({'Courses':["Spark","HAdoop","Python","pandas",None,"java",'pyspark'],
              'Fee':[20000,25000,26000,22000,np.nan,21000,22000],
              'Duration':["30days","40days","35days","40days"," ","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    })

row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
df

#df.iloc[starting : end row ,startColumn : endColumn]

df=pd.DataFrame(technologies,index=row_labels)
#below are quick example
df2=df.iloc[:,0:2]
df2

#this line uses the slicing operator to get DataFrame 
#items by index
#The first slice[:] indicates to return all rows
#the second slice specifies that only columns 
#between 0 and 2 (excluding) should be returned
#selection using index

df2=df.iloc[0:2,:]
df2

#slicing specific rows and specific columns using iloc attributes
df=pd.DataFrame(technologies,index=row_labels)
df
df3=df.iloc[1:2,1:3]
df3
 
#second operator [1:3] yields column 1 and 3 only
#select rows by integer index 
df2=df.iloc[2] #selecy row by index
df2

#select rows by index list 
df2=df.iloc[[2,3,6]]
df2

#select rows by integer index range
df2=df.iloc[1:5]
df2

#select first row
df2=df.iloc[:1]
df2

#select first three rows
df2=df.iloc[:3]
df2

#select last row
df2=df.iloc[-1:]
df2

#select last 3 rows
df2=df.iloc[-3:]
df2

#select alternate rows 
df2=df.iloc[::2]
df2

#loc 
'''selction using labels
In "loc" when we are giving label it will include last index 
bt in index(i.e.In "iloc") it will not consider last index
example 
iloc[0:2] == display 0 and 1 row data
loc[0:2] ===diaply 0,1,2 row data
'''
df=pd.DataFrame(technologies,index=row_labels)
df

#select rows by index labels it create series
df2=df.loc['r2']
df2

#select rows by label index
#here we have to use multiple rows so we use double [[]]
df2=df.loc[['r2','r3','r6']]
df2

#select rows by label index
df2=df.loc['r1':'r5']
df2

#select alternate rows
df2=df.loc['r1':'r5':2]
df2
'''
using loc[] to take column slices
loc[] syntax to slice columns
df.loc[:,start,end,step]
'''
df=pd.DataFrame(technologies,index=row_labels)
df

#select multiple columns
df2=df.loc[:,["Courses","Fee","Duration"]]
df2

#select column between two columns 
df2=df.loc[:,'Fee':'Discount']
df2

#select column by range 
df2=df.loc[:,'Duration':]
df2



#Pandas.DataFrame.query() 

#Query all rows with with cources equals to 'Spark'

import pandas as pd
import numpy as np 
technologies=({'Courses':["Spark","HAdoop","Python","pandas",None,"java",'pyspark'],
              'Fee':[20000,25000,26000,22000,np.nan,21000,22000],
              'Duration':["30days","40days","35days","40days"," ","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    })

row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
df

df2=df.query("Courses=='Spark'")
df2

#Query all rows with with cources not equals to 'Spark'

df2=df.query("Courses!='Spark'")
df2


#pandas add column to DataFrame
import pandas as pd
import numpy as np 
technologies=({'Courses':["Spark","HAdoop","Python","pandas",None,"java",'pyspark'],
              'Fee':[20000,25000,26000,22000,np.nan,21000,22000],
              'Duration':["30days","40days","35days","40days"," ","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
df
tutors=['Vedika',"Nikita","Vasudha","Vaishnavi","Ram","Sai","Rani"]
df2=df.assign(TutorsAssigned=tutors)
df2

#add multiple column to dataframes
MNCcompany=["TATA","HCL","Infosys","Google","Amazon","Microsoft","Flipkart"]
df2=df.assign(MNC=MNCcompany,Tutor=tutors)
df2

#derive 1 column from existing column

df=pd.DataFrame(technologies) 
df2=df.assign(Discount_percent=lambda x: x.Fee * x.Discount /100)
df2

#another way to add column
df=pd.DataFrame(technologies)
df["MNCcompany"]=MNCcompany
df


#add new col at specified position
#.insert(index,name,value)
df=pd.DataFrame(technologies)
df.insert(0,"Tutors", tutors)
df

#find out the number of rows and cols in DataFrame
rows_count=len(df.index)
rows_count

rows_count=len(df.axes[0])
rows_count

col_count=len(df.axes[1])
col_count

df=pd.DataFrame(technologies)
row_count=df.shape[0]
row_count

col_count=df.shape[1]
col_count

