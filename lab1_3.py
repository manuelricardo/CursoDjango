#!/usr/bin/env python
#-*- coding: utf-8 -*-

bstring = input('Ingrese el string de bits: ')

decimal = 0


exponent = len(bstring)-1

for digit in bstring:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent -1

print ('EL valor entero es: ', decimal)