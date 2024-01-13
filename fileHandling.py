# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:43:31 2023

@author: vaish
"""

with open('pi_digits.txt') as file_obj:
    #open() used to open file which we need 
    contents=file_obj.read()
print(contents)
#extra line is added at the eof

#to remove that extra line added use 'rstrip()'

with open('pi_digits.txt') as file_obj:
    #open() used to open file which we need 
    contents=file_obj.read()
print(contents.rstrip())

'''
Two types of path
1 relative path == 
        u have to put program n source file ib same folder then jst use filename
        u have to select workking path it only supported by vs code & pycharm
2 absolute path ==
         path from c drive c:/
linux & python support backward-slash path \\\
windows support  forward-slash path ///
when using virtual evironment use back slash as it is windows machine

'''

file_path="C:/1-python/pi_digits.txt"

with open(file_path) as file_obj:
    #open() used to open file which we need 
    contents=file_obj.read() 
print(contents.rstrip())

with open('pi_digits.txt') as file_obj:
    #open() used to open file which we need 
    for line in file_obj:
        print(line)
#extra line is added at the after each line
#remove white space use rstrip
with open('pi_digits.txt') as file_obj:
    #open() used to open file which we need 
    for line in file_obj:
        print(line.rstrip())

#working with file content
#print each line of file and comupte the length of data
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))
        
'''
one of the simple operation way to save data is to write it to file 
when u write text to file  the  output will still be avaliable after u 
close the terminal containing ur programs output
'''

#open file in write mode n write the content
filename="programming.txt"
with open(filename,'w') as file:
    file.write("I love programming")

#write method eraze all exsting file and write it
#write multiple lines here data will displayed horizontally
filename="programming.txt"
with open(filename,'w') as file:
    file.write("I love programming")
    file.write("I am coding in python")

#data will displayed vertically one below another
filename="programming.txt"
with open(filename,'w') as file:
    file.write("I love programming\n")
    file.write("I am coding in python\n")
    
#append() write file after eof
with open(filename,'a') as file:
    file.write("I love creating games\n")
    file.write("I also love to explore the things and create appps\n")

