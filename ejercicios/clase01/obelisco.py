#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:47:10 2021

@author: andrea
Twitter: @andreaquezadaa
"""

grosor_billete = 0.11 * 0.001  # grosor de un billete en metros
altura_obelisco = 67.5         # altura en metros
num_billetes = 1
dia = 1

while grosor_billete*num_billetes <= altura_obelisco:
    print(dia)
    dia = dia+1
    num_billetes = num_billetes*2

print(dia)