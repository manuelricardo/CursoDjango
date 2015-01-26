#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Program: Lab2_2.py
Author: Deiber Rincon

1. Ingresar el valor para saber el rango: 
2. Mostrar el tipo de calificación:

"""

number = int(input('Ingrese el número de su calificación: '))
if(number > 89):
	letter = 'S'
elif number >79:
	letter = 'A'
else:
	letter = 'Caso Perdido'
print('Su calificación está dentro del rango: ',letter)