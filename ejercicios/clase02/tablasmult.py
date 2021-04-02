#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:35:14 2021

@author: andrea

Twitter: @andreaquezadaa
"""

num = list(range(10))

table =[]

for element in num:
    table_n = []
    for number in num:
        mult = element * number
        table_n.append(mult)
    table.append (table_n)
    

for numero in num:
    print(f'{numero:>7d}', end= ' ')
    
print('---------- ---------- ---------- ---------- ---------- ----------')
for n, tabla in enumerate(table):
    print(f'{n}:{tabla}')
        

        
    
    

    


    