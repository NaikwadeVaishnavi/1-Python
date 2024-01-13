# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:36:48 2023

@author: vaish
"""


#seaborn
import seaborn  as sns
import pandas as pd
import matplotlib.pyplot as plt
#seaborn has 18 in-build dataset
#that can be found using following commands
sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()


#count plot
'''
count plot is helpful when dealing with categorical 
values it is used to plot the different category 
the column sex contain categories data in the titanic
data i.e. male female
'''
sns.countplot(x='sex',data=df)

#x=the name of the column 
#data - the dataframe
#hue categorial column to split the bar
#palette =color combination
#0 == death 1==survived

#palette='Setn' diff set of color comb where n is number
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')

sns.countplot(x='sex',hue='survived',data=df,palette='Set2')

sns.countplot(x='sex',hue='survived',data=df,palette='Set3')

#KDE plot kernal density estimate plot 
#used to plot distribution of contineous data

sns.kdeplot(x='age',data=df,color='black')

'''
x- name of column
data - dataframe
color -  color of the graph u can find all list of color
'''

#distribution plot == histogram
sns.displot(x='age',kde=True,bins=6,data=df)

'''
kde= it is set of false  by default however if u wish
bins= the no. of bins/bar
the lower the no. wider the bar and wider the interval
'''

sns.displot(x='age',kde=True,bins=5,
            hue=df['survived'],palette='Set1',data=df)

'''
scatter plot
for this plot and plots below 
we will be working with iris dataset
the iris dataset  contain data related to flower petal size 
'''

df=sns.load_dataset('iris')
df

#scattering using seaborn
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

#joint plot 
# a join plot is also used to plot correlation between dataset

sns.jointplot(x="sepal_length",y="petal_length",data=df,kind='reg')

sns.jointplot(x="sepal_length",y="petal_length",data=df,kind='hist')

sns.jointplot(x="sepal_length",y="petal_length",data=df,kind='kde')

'''
kind - the kind of plot to be plotted
it can be one of following
scatter hist hex kde reg resid

'''
#pair plot
sns.pairplot(df)

#heat map can be used to visualized confusion matrices

corr=df.corr()
sns.heatmap(corr)
