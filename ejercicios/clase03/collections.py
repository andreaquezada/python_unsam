#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:07:23 2021

@author: andrea

Twitter: @andreaquezadaa
"""

#%% Ejercicio 3.8
# No consigo quitar el código de escape de la lista row que se imprime en el Warning
import csv

def costo_camion(nombre_archivo):
    costo = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for n, line in enumerate(f, start=1):
        try:
            row = line.split(',')
            costo += float(row[1])*float(row[2])
        except ValueError:
            print(f'Fila {n}: No pude interpretar: {row}')
    f.close()
    return costo

costo = costo_camion('missing.csv')
    
#%% Ejercicio 3.9 Función zip()

def costo_camion(nombre_archivo):
    costo = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for n, line in enumerate(rows, start=1):
        record = dict(zip(headers, line))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo += ncajones * precio
        except ValueError:
            print(f'Fila {n}: No pude interpretar: {line}')
    return costo
        
costo = costo_camion('fecha_camion.csv')
print(costo)

#%% 3.11 Contadores
from collections import Counter

def leer_camion(nombre_archivo):
    '''Guarda los datos del archivo en una lista de tuplas. Cada tupla contiene los datos de cada fila'''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            lote = (record['nombre'], int(record['cajones']), float(record['precio']))
            camion.append(lote)
    return camion

camion = leer_camion('../Data/camion.csv')
camion2 = leer_camion('../Data/camion2.csv')

total_cajones = Counter()
for nombre, cajones, precio in camion:
    total_cajones[nombre] += cajones
print(total_cajones)

total_cajones2 = Counter()
for nombre, cajones, precio in camion2:
    total_cajones2[nombre] += cajones
print(total_cajones2)

todos_camiones = total_cajones + total_cajones2
print(todos_camiones)