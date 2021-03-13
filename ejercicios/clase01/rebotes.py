#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 19:55:45 2021

@author: andrea
Twitter: @andreaquezadaa
"""

altura_inicial = 100       # altura en metros
altura_rebote = 3/5               # alturas subsiguientes
numero_rebotes = 1

while numero_rebotes <= 10:
    nueva_altura = round(altura_inicial*altura_rebote, ndigits=4)
    print(nueva_altura)
    altura_inicial = nueva_altura
    numero_rebotes = numero_rebotes + 1