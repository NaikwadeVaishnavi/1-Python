# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:02:44 2023

@author: vaish
"""

import re
line='asdf fjdk; fjek,asdf,foo'
re.split(r'(?:,|;|\s)\s*',line)

##########
pattern=r'(?:,|;|\s)\s*'     
x=re.split(pattern,line)
print(x)

#matching txt at the start or end of  string 
filename='spam.txt'
filename.endswith('.txt')

#endswith
area_name='6 th lane west andheri'
area_name.endswith("west andheri")

#startswith
choice=('http:','ftp:')
url='http://www.python.org'
url.startswith(choice)

#slicing of string

s='ABCDEFGHI'
print(s[2:7]) #CDEFG

print(s[-7:-2]) #CDEFG

print(s[2:-5]) #CD

#steps in slicing
S='ABCDEFGHI'

print(S[2:7:2]) #CEG

print(S[6:1:-2])

print(S[:3])
        
print(S[6:])

print(S[::-1])

#similar operations can be done with slices

filename='span.txt'
filename[-4:]=='.txt'


url = 'http:/www.python.org'
url[:5]=='http:' or url[:6]=='https:' or url[:4]=='ftp:'

#package available to check the file extension
#pip install fnmatch2

from fnmatch import fnmatch, fnmatchcase 
names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]


from fnmatch import fnmatch,fnmatchcase
names = ['Andheri East','Parle East','Dadar West']
[name for name in names if fnmatch(name, '* East')]

addresses=[
            '5412 N CLARK ST',
            '1060 W ADDISON ST',
            '1039 W GRANVILLE AVE',
            '2122 N CLARK ST',
            '4802 N BROADWAY'
           ]
from fnmatch import fnmatch
[addr for addr in addresses if fnmatch(addr,'* ST')]
 
#

text='yeah but no, yeah ,but no,but yeah'
#exact match
text=='yeah'
#False 
#Match at start or end
text.startswith('yeah')
#True
text.endswith('no')
#False


text1='11/27/2012'
text2='Nov 27, 2012'

import re
#simple matching \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')
#yes
if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')
#no

datapat=re.compile(r'(\d+/\d+)/(\d+)')
if re.match(datapat, text1):
    print("yes")
else:
    print('no')
#yes
if re.match(datapat, text2):
    print("yes")
else:
    print('no')
#no

#searching and replacing text
text='yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')

#if u have data in format 11/27/2012 want to convert 2012-2013
#\3 3 rd group, \1 st gr
#today is 2012-11-27 PyCon starts 2013-3-13
#IF u want to know how many substitute are made in text 
#then  u can subn() method

text='Today is 11/27/2012. PyCon starts 3/13/2013'
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
#'Today is 2012-11-27. PyCon starts 2013-3-13'


text='UPPER PYTHON, lower python Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)
# ['PYTHON', 'python', 'Python']

#substitute python with snake
re.sub('python','snake',text,flags=re.IGNORECASE)
#'UPPER snake, lower snake Mixed snake'

'''the last example reverse a limitation that replacing 
text won't match the case of the matched text If u need 
to fix this u might have to use a support function
as the following'''

text
import re
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.capitalize()
        else:
            return word
    return replace
text3=re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
text3
#input == 'UPPER PYTHON, lower python Mixed Python'
#output =='UPPER SNAKE, lower Snake Mixed snake'

str_pat=re.compile(r'\"(.*)\"')
text1='Computer says "no."'
str_pat.findall(text1)        #['no.']

text2='Computer says "no." Phone says "yes."'
str_pat.findall(text2)
str_pat=re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
#['no.', 'yes.']


str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
#['no.', 'yes.']

comment=re.compile(r'/\*(.*?)\*/')
text1='/*this is a multiline comment*/'
comment.findall(text1)
#['this is a multiline comment']

text2='''/*this is a 
 multiline comment*/'''
comment=re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)
#['this is a \n multiline comment']


comment=re.compile(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)
#['this is a \n multiline comment']

s1='Spicy jalao'
