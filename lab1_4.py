#-*- coding: utf-8 -*-

decimal = int(input("Ingrese el número decimal a convertir: "))

if decimal == 0:
	print(0)

else:
	print ('Resto del cociente binario')
	bstring = ""

	while decimal > 0:
		remainder = decimal % 2
		decimal = decimal // 2
		bstring = str(remainder) + bstring

		print ("%1d%1d%2s" % (decimal,remainder,bstring))

	print ("La representación binaria es: ", bstring)