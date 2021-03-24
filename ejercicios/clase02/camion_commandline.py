#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:11:39 2021

@author: andrea

Twitter: @andreaquezadaa
"""
#%%
import csv
import sys

def costo_camion(nombre_archivo):
    costo = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for line in f:
        try:
            row = line.split(',')
            costo += float(row[1])*float(row[2])
        except ValueError:
            print(f'Aviso: hay datos faltantes en la fila {row[0]}')
    f.close()
    return costo

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'
    
costo = costo_camion(nombre_archivo)
print(f'Costo total: {costo}')