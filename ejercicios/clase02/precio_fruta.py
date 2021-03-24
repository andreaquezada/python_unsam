#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:16:25 2021

@author: andrea

Twitter: @andreaquezadaa
"""
#%% naranja - simple
with open('precios.csv', 'rt') as g:
    for line in g:
        row = line.split(',')
        if row[0] == 'Naranja':
            print('El precio de la naranja es:',row[1])
            

#%% dos with
def buscar_precio(fruta):
    with open('precios.csv', 'rt') as g:
        if fruta not in g.read():
            print(fruta, 'no figura en el listado de precios')
    with open('precios.csv', 'r') as f:
        for line in f:
            if fruta in line:
                row = line.split(',')
                print('El precio de un cajón de', fruta, 'es:', row[1], end='')
#%% diccionario
## No entiendo porque el index 1 no funciona y el -1 si
def dar_precio(fruta):
    fruta_precios = {}
    with open('precios.csv', 'rt') as f:
        for line in f:
            row = line.split(',')
            fruta_precios[row[0]] = row[-1].strip()
    if fruta in fruta_precios.keys():
        print(f'El precio de un cajón de {fruta} es {fruta_precios[fruta]}', end = '')
    else:
        print(f'{fruta} no figura en el listado de precios', end = '')
                
        
