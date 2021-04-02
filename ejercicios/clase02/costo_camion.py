#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:34:57 2021

@author: andrea

Twitter: @andreaquezadaa
"""
#%% basico
costo = 0

with open('camion.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        costo += float(row[1])*float(row[2])
        
print('Costo total', round(costo, 2))

#%% función
def costo_camion(nombre_archivo):
    costo = 0
    with open(nombre_archivo, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            costo += float(row[1])*float(row[2])
        return costo
#%% missing data basico

costo = 0

with open('missing.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        try:
            row = line.split(',')
            costo += float(row[1])*float(row[2])
        except ValueError:
            print(f'Aviso: hay datos faltantes en la fila {row[0]}')
        
print('Costo total', round(costo, 2))

#%% missing data función

def costo_camion(nombre_archivo):
    costo = 0
    with open(nombre_archivo, 'rt') as f:
        headers = next(f)
        for line in f:
            try:
                row = line.split(',')
                costo += float(row[1])*float(row[2])
            except ValueError:
                print(f'Aviso: hay datos faltantes en la fila {row[0]}')
        return costo
#%% modulo csv

import csv

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
costo = costo_camion('camion.csv')
print(costo)
    