# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:36:19 2023

@author: vaish
"""

from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader

#creating a pdf reader object
reader=PdfReader("python_tutorial.pdf")

#print no. of pages in pdf file
print(len(reader.pages))

#getting a specific page from the pdf file
page=reader.pages[10]

#extract the text from page
text=page.extract_text()
print(text)

#extract num   
import re
chat='Hi:I have problem with my order number 41288912'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat)
matches

import re
chat='Hi:I have problem with my order number 41288912'
pattern='order [a-z]* (\d*)'
matches=re.findall(pattern,chat)
matches

import re
chat2='Hi:I have problem with my order number # 41288912'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches

import re
chat3='Hi: my order number 41288912 is having issue I was charged 300$ when 12105313'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat3)
matches

def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat)
