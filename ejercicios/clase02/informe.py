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
    '''Guarda los datos del archivo en una lista de diccionarios.'''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {'nombre':row[0], 'cajones':int(row[1]), 'precio':float(row[2])}
            camion.append(lote)
    return camion

#%% Balance del negocio
from collections import Counter
import csv
import pprint as pp
from tabulate import tabulate
import numpy as np

def leer_camion(nombre_archivo):
    '''Guarda los datos del archivo en una lista de tuplas. Cada tupla contiene los datos de cada fila'''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion

def leer_precio(nombre_archivo):    
    ''' Crea un diccionario de precios con los nombres de las frutas como keys.'''
    precio_venta = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                precio_venta[row[0]] = float(row[1].strip())
            except IndexError:
                pass
    return precio_venta

camion = leer_camion('camion.csv')
precio_venta = leer_precio('precios.csv')

total_cajones = Counter()
total_precio = Counter()     
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones
    total_precio[nombre] += n_cajones*precio

ganancias = []
for element in precio_venta.keys():
    try:
        precio_compra = total_precio[element]/total_cajones[element]
        balance = precio_venta[element] - precio_compra
        ganancia_total = balance * total_cajones[element]
        ganancias.append([element, total_cajones[element], precio_compra, precio_venta[element], balance, ganancia_total])
    except ZeroDivisionError:
        pass
print(tabulate(ganancias, headers=['Fruta', 'Cajones', 'Precio de compra', 'Precio de venta', 'Ganancia neta']))
      


    
 

#%%


def precio_total(nombre_archivo):
    ''' Computa el gasto que se hizo en cada fruta multiplicando los cajones por el costo de cada uno'''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            ncajones = int(row[1])
            precio = float(row[2])
            total = (row[0], ncajones, ncajones * precio)
            camion.append(total)
    return camion

camion = precio_total('camion.csv')

total_cajones = Counter()            
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones