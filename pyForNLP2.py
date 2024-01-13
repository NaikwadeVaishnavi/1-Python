# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:36:19 2023

@author: vaish
"""

#Elon musk data
import re
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family
'''

def get_pattern_match(pattern,text):
    matches=re.findall(pattern ,text)
    if matches:
        return matches[0]
get_pattern_match(r'age (\d+)',text)#age
get_pattern_match(r'Born(.*)\n',text).strip()#full name
get_pattern_match(r'Born.*\n(.*)\(age', text).strip()#birth date
get_pattern_match(r'\(age.*\n(.*)', text)#birth place


#alternate way using fun and dicty
def extract_personal_info(text):
    age=get_pattern_match(r'age (\d+)',text)
    full_name=get_pattern_match(r'Born(.*)\n',text).strip()
    birth_date=get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
    birth_place=get_pattern_match(r'\(age.*\n(.*)', text)
    return {
        'age':int(age),
        'Full Name':full_name.strip(),
        'Birth Date':birth_date.strip(),
        'Birth Place':birth_place.strip()
        }
extract_personal_info(text)

#mukesh dhirubhai ambani
text='''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''
def extract_personal_info(text):
    age=get_pattern_match(r'age (\d+)',text)
    full_name=get_pattern_match(r'Born(.*)\n',text).strip()
    birth_date=get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
    birth_place=get_pattern_match(r'\(age.*\n(.*)', text)
    return {
        'age':int(age),
        'Full Name':full_name.strip(),
        'Birth Date':birth_date.strip(),
        'Birth Place':birth_place.strip()
        }
extract_personal_info(text)


#split the txt n print list of words in the  sentence
txt='Welcome to the new year 2023'
x=txt.split()
print(x)

'''
Removing special character

special character as u know 
are non-aplphanumeric character 
these character are most often found in comment
references currency number etc
these character add non value to text understanding
and induce noise into algorithm
for that regex package is used
'''

#remove special char
#in o/p it is observe that , . ? ! are present there cause they are included in exp
import re
def remove_special_char(txt):
    #define pattern
    pat=r'[^a-zA-z0-9.,!?/:;\"\'s]'
    return re.sub(pat,' ', txt)
remove_special_char('007 Not sure@ if this %was #fun 558923 What do #you think** of it.? $500USD!')

#split
txt='Welcome: to the, new year: 2023!'
x=re.split(r'(?:,|;|\s)\s*',txt)
print(x)

#remove num
import re
def remove_num(txt):
    #definr pattern to keep
    pattern=r'[^a-zA-z.,!?/:;\"\'s]'
    return re.sub(pattern,' ',txt)
remove_num('Welcome to the new year 2023')

#bigram trigram tokenization
'''
steaming== process of transforming word into best form 
like I worked I ate I eat

lamatization== additional to extract base,work

name-entity-relation
multi word expression tokeniser
certain gr of multiple words are treated as one entity

regular exp tokeniser sentences are split based on occurance of pattern

white space tokeniser split screen whereever there is space

bag of words process of converting unstructure data into 
structured form 

stop words words dsuch as articles and prepositions calles stop words
ex. was is were

'''

import string
def remove_punctuations(txt):
    txt=''.join([c for c in txt if c not in string.punctuation])
    return txt
remove_punctuations('Article: @First sentence of some,{important} article having lot of ~punctuations.And another one;!')

#review following
#nltk stemming
import nltk
def get_stem(txt):
    stemmer=nltk.porter.PorterStemmer()
    txt=' '.join ([stemmer.stem(word) for word in txt.split()])
    return txt
get_stem('We are eating and swimming; we have been eating and swimming he eats and swims; he eats and sweet; he ate and swam')


