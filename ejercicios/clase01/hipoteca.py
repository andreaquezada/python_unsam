#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)
Twitter: @andreaquezadaa
"""

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
mes = 0

while saldo > pago_mensual:
    mes = mes + 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    print(mes, round(total_pagado, 4), round(saldo, 4))
else:
    mes = mes + 1
    pago_mensual = saldo * (1+tasa/12)
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    print(mes, round(total_pagado, 4), round(saldo, 4))
    
          
print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses')