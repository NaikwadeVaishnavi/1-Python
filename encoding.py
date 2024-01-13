# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:21:48 2023

@author: vaish
"""
'''
unicode-8
unicode-16
UTF UNICODE TRANSFIRMATION FORMAT
UTF-8 8-bit values  are used in encoding unicode char
'''

str1='apple'
str2='jeei125'
str3='12345'
str4='pre@12'

str1.encode(encoding='UTF-8',errors='strict') #b'apple'
str2.encode(encoding='UTF-8',errors='strict') #b'jeei125'
str3.encode(encoding='UTF-8',errors='strict') #b'12345'
str4.encode(encoding='UTF-8',errors='strict') #b'pre@12'

text='one 🐘 and three 🐋'
print(text)
print(len(text))

''' we encode the string into a bytes type using the utf8 
encoding and print the bytes.
We count the number of bytes in this encoding types
'''

e=text.encode('utf8')
print(e) #in o/p u get encoded part
print(len(e))

fname='data1.txt'
with open (fname,mode='rb') as f:
    #by default it encoded in utf-8
    contents=f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))    

#for UTF-16 = change the encoding type of the file
fname='data.txt'
with open (fname,mode='rb') as f:
    #mode='rb' == reading binary
    #by default it encoded in utf-16
    contents=f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf16'))    

#text encoding NFC and NFD
'''
What is NFD and NFC?
Normalization Form D (NFD) Canonical Decomposition. 
Normalization Form C (NFC) Canonical Decomposition, 
followed by Canonical Composition.

there is no difference between NFC and NFD intended for 
generating code compatibale to platform
'''

#strapping-remove unwanted data-remove unnecessary white space
s=' hello world '
s.strip()
#hello world \n
s=' hello world \n'
s.lstrip() #remove left white space
s.rstrip() #remove right white space

#character stripping
t='----hello===='
t.strip('-') #remove all '-'
t.strip('-=') #remove both '-='

s='hello world'
s.replace(' ','')#'helloworld' replace white-space with no-space

import re
re.sub('\s+',' ',s) #\s any whitespace #'helloworld'


#alining the text string
text='hello world'
#20 for move upto 20char
text.ljust(20) #'hello world         '
text.rjust(20)#'         hello world'
text.center(20,'*')#'****hello world*****'

#format here ur data move upto given range
format(text,'>20')#'         hello world' #right adjected/align
format(text,'<20')#'hello world         ' #left adjested/align
format(text,'^20')#'    hello world     '#center align

format(text,'=>20s')#'=========hello world'
format(text,'=<20')#'hello world========='
format(text,'*^20')# '****hello world*****'

#these format codes can also be used in the format() method
#values. For example:
#s=spaces : == form 0 to given num
'{:>10s} {:>10s}'.format('Hello','World')#'     Hello      World'

x=1.2345
format(x,'>10') #'    1.2345'
format(x,'^10.2f')#'   1.23   '

parts=['Is','Chicago','Not','Chicago?']
' '.join(parts)
#'Is Chicago Not Chicago?' 
#join list element with adding whitespace

','.join(parts)
#'Is,Chicago,Not,Chicago?'
#join list element with ,

#if u join very few strings then u can use + operator




