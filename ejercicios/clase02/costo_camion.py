#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:34:57 2021

@author: andrea

Twitter: @andreaquezadaa
"""
costo = 0

with open('camion.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        costo = costo + float(row[1])*float(row[2])
        
print('Costo total', round(costo, 2))