#Entrada de datos del usuario

options = print("Elija las siguientes operaciones")
operations = int(input("1: Suma, 2:Resta, 3:Multiplicación, 4:División: "))


while True:
	if operations == 1:
		num1 = int(input("primer numero para sumar: "))
		num2 = int(input("segundo numero para sumar: "))
		resultado = num1+num2
		print(f"El resultado de la suma es {resultado}")
		options = print("Elija las siguientes operaciones: ")
		operations = int(input("1: Suma, 2:Resta, 3:Multiplicación, 4:División: "))

	elif operations == 2:
		num1 = int(input("primer numero para resta: "))
		num2 = int(input("segundo numero para resta: "))
		resultado = num1-num2
		print(f"El resultado de la resta es {resultado}")
		options = print("Elija las siguientes operaciones: ")
		operations = int(input("1: Suma, 2:Resta, 3:Multiplicación, 4:División: "))

	elif operations == 3:
		num1 = int(input("primer numero para multiplicar: "))
		num2 = int(input("segundo numero para multiplicar: "))
		resultado = num1*num2
		print(f"El resultado de la Multiplicación es {resultado}")
		options = print("Elija las siguientes operaciones: ")
		operations = int(input("1: Suma, 2:Resta, 3:Multiplicación, 4:División: "))

	elif operations == 4:
		num1 = int(input("primer numero para dividir: "))
		num2 = int(input("segundo numero para divir: "))
		resultado = num1/num2
		print(f"El resultado de la división es {resultado}")
		options = print("Elija las siguientes operaciones: ")
		operations = int(input("1: Suma, 2:Resta, 3:Multiplicación, 4:División: "))

	else:
		print("No se encontro la operación elegida")
		options = print("Elija las siguientes operaciones")
		operations = int(input("1: Suma, 2:Resta, 3:Multiplicación, 4:División: "))
		
		
	

