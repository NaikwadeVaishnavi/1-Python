
'''  
create dataframe from 
dict={
'x':[78,85,96,80,86]
'y':[84,94,89,83,86]
'z':[86,97,96,72,83]
}
'''
import pandas as pd
import numpy as np
sample=({
'x':[78,85,96,80,86],
'y':[84,94,89,83,86],
'z':[86,97,96,72,83],
})
df=pd.DataFrame(sample)
df


#create dataframe 
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita"," dha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,np.nan,1,1,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df

print("Summary of data basic information about dataframe")
df.describe()
df.info()

#program to get first 3 rows
df.iloc[:3]

#select name and score col from given dataframe
df[["Name","Score"]]

#select specifid col and row (score & qualify)
df[["Score","Qualify"]]
df.iloc[1::2,::2]
 
#program to select row where no. of attempt are greater than 2
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df
print("row where no. of attempt are greater than 2")
df[df['Attempts']>2]

#other method using .loc()
df2=df.loc[df.Attempts>2]
df2

#print no. of rows and columns
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df
#row count
row_cnt=len(df.index)
row_cnt

#row count
row_cnt=df.shape[0]
row_cnt

#row count
row_cnt=len(df.axes[0])
row_cnt

#column count
col_cnt=len(df.axes[1])
col_cnt
 
#column count
col_cnt=df.shape[1]
col_cnt

print("Number of rows in dataframe :",row_cnt)
print("Number of cols in dataframe :",col_cnt)


col_count=df.shape[1]
col_count

#program to select the rows where score is missing
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df

print("Print row with score is NULL")
df[df["Score"].isnull()]

#program to search row with score between 50-90
print("Row with score between 50-90(inclusive)")
df[df["Score"].between(50,90)]

#select rows whose attempts less than 2 and score grater than 75
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df

print("less than 2 attempts and score greater than 80")
df[(df["Attempts"]<2) & (df['Score']>=80)] 

#program to change score of row b to 85
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df

print("change score of row b to 85")
df.loc["b","Score"]=85
df

#calculate sum of exam attempt
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df

print("Sum of number of total attempts")
df['Attempts'].sum()

#calculate mean of score
print("Mean  of score")
df['Score'].mean()

#program to append new row
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df
#append new row to dataframe
df.loc['f']=['Sai',67,1,'No']
print("After appending new row obtained dataframe\n",df)
 
#sort values by first name in descending order and score by ascending
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df

print("sort values by first name in descending order and score by ascending")
df2=df.sort_values(by=["Name","Score"], ascending=[False,True])
df2
df.sort_values(by=["Name"], ascending=[False])
df.sort_values(by=["Score"], ascending=[True])

#program to replace qualify column content the values yes&no with true&fasle
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df

print("replace qualify column content the values yes&no with true&fasle")

df["Qualify"]=df["Qualify"].map({'Yes':True,'No':False})
df

#program to change name sai with sairaj
df["Name"]=df["Name"].replace("Sai","Sairaj")
df

#search panda program to insert new column in existing 
Grade=["A","B","C","A","B","D"]
df['Grade']=Grade
print("Add new col to dataframe")
df

#program to iterate over row dataframe
import pandas as pd
import numpy as np
exam_data={"Name":['Vedika',"Nikita","Vasudha","Vaishnavi","Ram"],
           "Score":[98,np.nan,78,89,45],
           "Attempts":[1,4,1,3,2],
           "Qualify":["Yes","No","Yes","No","Yes"]}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data ,index=row_labels)
df

for index,row in df.iterrows():
    print(row["Name"],row["Score"])

