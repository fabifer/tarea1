# -*- coding: utf_8 -*-
# primos.py: muestra los numeros primos hasta n

from math import sqrt

n = int(raw_input ("Ingrese un numero natural: "))

print ("Primos hasta " + str(n) + ":")

for x in range(2,n+1):

	es_primo = True

	for y in range(2,int(sqrt(x))+1):
		if x % y == 0:
			es_primo = False
			break

	if es_primo:
		print(x)
