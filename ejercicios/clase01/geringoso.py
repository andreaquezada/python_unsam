#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 20:08:50 2021

@author: andrea
Twitter: @andreaquezadaa
"""

cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    if c == 'a':
        capadepenapa = capadepenapa + 'apa'       
    elif c == 'e':
        capadepenapa = capadepenapa + 'epe'
    elif c == 'i':
        capadepenapa = capadepenapa + 'ipi'
    elif c == 'o':
        capadepenapa = capadepenapa + 'opo'
    elif c == 'u':
        capadepenapa = capadepenapa + 'upu'       
    else:
        capadepenapa = capadepenapa + c
print(capadepenapa)