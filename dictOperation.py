# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:42:32 2023

@author: vaish
"""

'''
PROGRAM to add key to dict
ip={0:10,1:20}
op={0:10,1:20,2:30}
'''
ip={0:10,1:20}
ip.update({2:30})
print(ip)

#alternate way

ip[2]=30
print(ip)

'''
program to concat the foll dict
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
'''

d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4={}
for i in (d1,d2,d3):d4.update(i)
print(d4)

'''
check whether given key exist in dict or not
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key(x):
    if x in d:
        return True
    else:
        return False
is_key(5)
is_key(9)

'''
program to iterate a key and value using for loop
'''
d={'x':0,"y":20,'z':30}
for d_key,d_val in d.items():
    print(d_key,":",d_val)

