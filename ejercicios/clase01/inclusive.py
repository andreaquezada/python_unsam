#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 00:39:14 2021

@author: andrea

Twitter: @andreaquezadaa
"""

frase = '¿Cómo transmitir a los otros el infitino Aleph?'
palabras = frase.split()
nueva_frase = []

for palabra in palabras:
    if  palabra[-1] == 'o':
        nueva_palabra = palabra[:-1]+palabra[-1].replace('o','e')    
    elif palabra[-2] == 'o':
        nueva_palabra = palabra[:-2]+palabra[-2].replace('o','e')+palabra[-1]
    else:
        nueva_palabra = palabra
    nueva_frase.append(nueva_palabra)
    
frase_t = ' '.join(nueva_frase)
print(frase_t)

#%%

