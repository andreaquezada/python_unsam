#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:51:55 2021

@author: andrea

Twitter: @andreaquezadaa
"""
#%%
import csv

def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            ncajones = int(row[1])
            precio = float(row[2])
            total += ncajones * precio
    return total
#%% 
import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion
#%%
import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {'nombre':row[0], 'cajones':int(row[1]), 'precio':float(row[2])}
            camion.append(lote)
    return camion

#%%
import csv

def leer_precio(nombre_archivo):    
    fruta_precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                fruta_precios[row[0]] = row[1].strip()
            except IndexError:
                pass
    return fruta_precios
#%% Balance
total = 0.0
for s in camion:
    total += s['cajones']*s['precio']

print(total)

