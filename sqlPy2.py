# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:19:49 2023

@author: vaish
"""

import psycopg2 as pg2
conn = pg2.connect(database = 'dvdrental',user='postgres', password = 'root')

cur=conn.cursor()

cur.execute(''' create table courses1(
    courses_id serial primary key,
    course_name varchar (50) unique not null,
    course_instructoe varchar(100) not null,
    topic varchar (20) not null);
            ''')
conn.commit()
cur.close()
