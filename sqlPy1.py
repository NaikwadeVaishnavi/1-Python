# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:58:03 2023

@author: vaish
"""
import psycopg2 as pg2

#Creating a connection with postgreSQl
# Password is whatever password you set
#we can see password in install
conn=pg2.connect(database='dvdrental',user='postgres',password="root")
cur=conn.cursor()

# Pass in a postgreSQl query as a string
cur.execute("SELECT * from payment")

#Return a tuple of the  first row as a python objects
cur.fetchone()


#Return All rows at once
cur.fetchall()


#To save and index results assign it to a varaiable
data= cur.fetchmany(10)

#Dont forget to close the connection
#Willing the kernal or shutting down jupyter will also close it
conn.close()
