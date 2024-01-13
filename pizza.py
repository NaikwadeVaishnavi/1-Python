# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:20:35 2023

@author: vaish
"""
'''
file is imported in session4
'''

def make_pizza(size,*toppings):
   print(f"\nMaking a {size}-inch with the following toppings:")
   for topping in toppings:
       print(f"-{toppings}")
