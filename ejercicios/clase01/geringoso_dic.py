#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:40:56 2021

@author: andrea

Twitter: @andreaquezadaa
"""
#%%
lista_palabras = ['luna', 'camión', 'fruta', 'rojo', 'calcetín', 'soñar']
#%% 

def geringoso(lista_palabras):
    cadenas = {}
    for e in lista_palabras:
        capadepenapa = ''
        for c in e:
            if c.lower() in 'aeiouáéíóú':
                capadepenapa += c + 'p' + c
            else:
                capadepenapa += c
        cadenas[e] = capadepenapa  
    print(cadenas)
#%%
print(cadenas)
