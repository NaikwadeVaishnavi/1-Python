# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:19:19 2023

@author: vaish
"""
# Python for NLP
'''
Natural Lang. Processing 
data extraction from = text audio video

tesla company filing - sec filing - annual /quaterly report - apply filter-10Q- (pdf)
regex101.m

'''

# install regex - pip install regex

# extract phone no. in indian format

import re
text = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

# \d matches a digit (equivalent to [0-9])
pattern = '\d\d\d\d\d\d\d\d\d\d'
# alternate way
pattern = '\d{10}'

matches = re.findall(pattern, text)
matches


text1 = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''


'''
\(\d{3}\)-\d{3}-\d{4}|\d{10}
\( matches the character ( with index 4010 (2816 or 508) literally (case sensitive)
\d matches a digit (equivalent to [0-9])
{3} matches the previous token exactly 3 times
\) matches the character ) with index 4110 (2916 or 518) literally (case sensitive)
- matches the character - with index 4510 (2D16 or 558) literally (case sensitive)
\d matches a digit (equivalent to [0-9])
{3} matches the previous token exactly 3 times
- matches the character - with index 4510 (2D16 or 558) literally (case sensitive)
\d matches a digit (equivalent to [0-9])
{4} matches the previous token exactly 4 times
2nd Alternative \d{10}
\d matches a digit (equivalent to [0-9])
{10} matches the previous token exactly 10 times
'''

pattern = '\(\d{3}\)-\d{3}-\d{4}'

matches = re.findall(pattern, text)
matches


'''\d{3}-\d{3,4}
\d matches a digit (equivalent to [0-9])
{3} matches the previous token exactly 3 times
- matches the character - with index 4510 (2D16 or 558) literally (case sensitive)
\d matches a digit (equivalent to [0-9])
{3,4} matches the previous token between 3 and 4 times, as many times as possible, giving back as needed (greedy)
'''
pattern = '\d{3}-\d{3,4}'
matches = re.findall(pattern, text)
matches

# either a|b expression use or('|') operator
''' \(\d{3}\)-\d{3}-\d{4}|\d{10}
1st Alternative \(\d{3}\)-\d{3}-\d{4}
\( matches the character ( with index 4010 (2816 or 508) literally (case sensitive)
\d matches a digit (equivalent to [0-9])
{3} matches the previous token exactly 3 times
\) matches the character ) with index 4110 (2916 or 518) literally (case sensitive)
- matches the character - with index 4510 (2D16 or 558) literally (case sensitive)
\d matches a digit (equivalent to [0-9])
{3} matches the previous token exactly 3 times
- matches the character - with index 4510 (2D16 or 558) literally (case sensitive)
\d matches a digit (equivalent to [0-9])
{4} matches the previous token exactly 4 times

2nd Alternative \d{10}
\d matches a digit (equivalent to [0-9])
{10} matches the previous token exactly 10 times
'''
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches = re.findall(pattern, text)
matches

'''
Let's try 
following pattern
A protracted; legal battle; over a 32-carat;
 Golconda diamond-

We want any character  except ; and - 
pattern  will be [^;-] 
goto regular expression window and try this 
'''
# when we dont want any char we use ^ as Esc char
'''
[^;-]
Match a single character not present in the list below [^;-]
;- matches a single character in the list ;- (case sensitive)'''

text2 = '''A protracted; legal battle; over a 32-carat;
 Golconda diamond-'''
pattern = '[^;-]'
matches = re.findall(pattern, text2)
matches

# Extract Note 1 – Summary of Significant Accounting Policies
text3 = '''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
'''
# for '-' their is unicode compile error so u have to rewrite that hyphen(-)

pattern = 'Note \d - [^\n]'
matches = re.findall(pattern, text3)
matches  # ['Note 1 - S']

pattern = 'Note \d - [^\n]+'
matches = re.findall(pattern, text3)
matches  # ['Note 1 - Summary of Significant Accounting Policies']

pattern = 'Note \d - [^\n]*'
matches = re.findall(pattern, text3)
matches  # ['Note 1 - Summary of Significant Accounting Policies']


#when u want only one line not next line use [^\n]

#pattern == capture everything enclosed(....)
#(regular exp) here () used as capture encloses
#it will only print enclosed reg. exp. data
'''
Note \d - ([^\n]+)  
Note  matches the characters Note  literally (case sensitive)
\d matches a digit (equivalent to [0-9])
 -  matches the characters  -  literally (case sensitive)
1st Capturing Group ([^\n]+)
Match a single character not present in the list below [^\n]
+ matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)
\n matches a line-feed (newline) character (ASCII 10)
'''
pattern = 'Note \d - ([^\n]+)'
matches = re.findall(pattern, text3)
matches  # ['Summary of Significant Accounting Policies']

#print quaters of the academic year
text4='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
#quaters can be Q1 Q2 Q3 or Q4 not Q5 Q6

pattern='FY\d{4} Q\d'
matches=re.findall(pattern, text4)
matches #['FY2021 Q1','FY2020 Q4','FY2021 Q1','FY2020 Q4']

#single chaeacter a,b or c[abc]
#try pattern 'FY\d{4} Q[1,2,3,4]'
pattern='FY\d{4} Q[1,2,3,4]'
matches=re.findall(pattern, text4)
matches # ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']

#u can also give range
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern, text4)
matches # ['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']

#now let us assume we want only 2021 Q1 and 2020 Q4 then 
#u can get extract through(...)
text5='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''

pattern1='FY\d{4} Q[1-4] |fy\d{4} Q[1-4]'
matches=re.findall(pattern1, text5)
matches #['FY2021 Q1 ', 'fy2020 Q4', 'FY2021 Q1 ', 'fy2020 Q4']

matches=re.findall(pattern, text5,re.IGNORECASE)
matches#['FY2021 Q1 ', 'fy2020 Q4', 'FY2021 Q1 ', 'fy2020 Q4']

#o/p like '2021 Q1', '2020 Q4'
#uses extract operator (...)
pattern1='FY(\d{4} Q[1-4])'
matches=re.findall(pattern1, text5,re.IGNORECASE)
matches #['2021 Q1', '2020 Q4', '2021 Q1', '2020 Q4']

#we want to $4.85 and $3 
#simply $ can not be used as it is special symbol
#Even .character can not br used it is also special symbol
text6='''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
pattern='\$[0-9\.]+'
matches=re.findall(pattern, text6)
matches  #['$4.85', '$3', '$4.85', '$3']

#if we dont want $ 
pattern='\$([0-9\.]+)'
matches=re.findall(pattern, text6)
matches #['4.85', '3', '4.85', '3']


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
chat3='Hi: my order number 41288912 is having issue I was charged 300$ when online it is 200$'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat3)
matches

def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat)

#retrive email id and phone no.
#HW
chat1="Hi: u ask lot of que 1234567891, abc@xyz.com"
chat2="Hi: here it is: (123) -567-8912, abc@xyz.com"
chat3="Hi:phone: 1234567891 email: abc@xyz.com"

pattern1='[a-z]*\@[a-z]*\.com'
get_pattern_match(pattern1,chat1)

get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d')
