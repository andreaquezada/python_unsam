#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:19:08 2021

@author: andrea

Twitter: @andreaquezadaa
"""

# solucion de errores

#%% Ejercicio 3.1 Función tiene_a()
''' Comentario: La función solo arroja un error semántico. Arroja False cuando la
 expresión no comienza con la letra a porque el contador estaba fuera del loop 
 while-else y no iteraba toda la expresión.
   Lo corregí moviendo el contador dentro del loop.'''
# Función corregida:
def tiene_a(expresion): 
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False
    
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%% Ejercicio 3.2 Funcion tiene_a()
'''Comentario: La función arroja cuatro SyntaxError: invalid syntax. Tres de ellos
debido a la falta de semicolones en la línea que define la función y las lineas
de los loops while e if. El cuarto se debe a que se usa = en vez de == para comparar
los valores '''
# Función corregida:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#%% Ejercicio 3.3 Función tiene_uno
'''Comentario: La función arroja un TypeError en la tercera expresion (1984) 
porque se trata de un integral. 
    Lo corregí adañiendo las comillas para que fuera un string
'''
# Funcion corregida

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%% Ejercicio 3.4 Función suma
''' Comentario: Se trata de un error semántico que viene de que la función suma
no regresa ningún valor.
    Lo corregí añadiendo return c al final del código'''

def suma(a,b):
    c = a + b
    return c


a = 2
b = 3
c = suma(a,b)

print(f"La suma da {a} + {b} = {c}")

#%% Ejercicio 3.5 
''' Comentario: Error semántico debido a que se inicializa el diccionario
 registro al principio de la función, se itera sobre el archivo y se van 
 reasignando los valores asociados a las claves del diccionario. 
     Lo solucioné inicializando el diccionario dentro del loop for.
'''
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('camion.csv')
pprint(camion)

        