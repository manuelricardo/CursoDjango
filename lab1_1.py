# -*- coding: utf-8 -*-
"""
Program: lab1_1.py
Author: Manuel Avila

Calcular la tasa de impuesto de un alimento

1. Decalaración de vaiables:
			tax tasa de impuesto
			tax_one tasa de impuesto adicional

2. Entradas
			valor del alimento
			numero de alimentos

3. Computación:
			tasa de entrada = suma de alimentos + tax + tax_one

4. Salida: 
			El cálculo de los elementos comprados
"""
# Declaración de constantes
TAX = 0.16
TAX_ONE = 0.03

# Entrada(s) del teclado

food = int(input('Ingrese el valor del Alimento: '))

amount_food = int(input('Ingrese la cantidad de alimentos: '))

# Cómputos

total = (food * amount_food) * (TAX+TAX_ONE)

print ("El total de sus impuestos es: ", total)
