# -*- coding: utf_8 -*-
# fibonacci.py: muestra los numeros de fibonacci hasta n

fib1 = 0
fib2 = 1
temp = 0


n = int(raw_input("Ingrese un numero natural: "))

print ("Serie de Fibonacci hasta " + str(n) + ": ")

if n >= 0:

	print (fib1)

	if n >= 1:

		print(fib2)

		for x in range(2, n+1):
			temp = fib2 + fib1
			print(temp)
			fib1 = fib2
			fib2 = temp
