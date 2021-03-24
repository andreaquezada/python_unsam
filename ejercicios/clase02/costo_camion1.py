#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:58:46 2021

@author: andrea

Twitter: @andreaquezadaa
"""


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