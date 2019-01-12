opcion=0

Agenda={"Walter White":"912345678","Jesse Pinkman":"923456789","Skyler White":"998765432","Hank Schrader":"999123675"}

while opcion!=4:
	print("\nAGENDA")
	print("1- Ver agenda\n2- Añadir número\n3- Eliminar número\n4- Salir")
	opcion=int(input("Ingrese un opción: "))

	if opcion==1:
		print(Agenda)
	elif opcion==2:
		nombre=input("\nIngrese el nombre: ")
		apellido=input("Ingrese el apellido: ")
		numero=input("Ingrese el numero: ")
		if numero[0]=="9" and len(numero)==9 and numero.isdigit() and (nombre+" "+ apellido not in Agenda):
			Agenda[nombre+ " " + apellido]=numero
			print("\nContacto añadido exitosamente")
		else:
			print("\nNúmero incorrecto y/o contacto repetido\nERROR AL AÑADIR CONTACTO")
	elif opcion==3:
		print(Agenda.keys())
		print("Ingrese los nombres y apellidos a eliminar\n")
		nombre=input("Ingrese el nombre: ")
		apellido=input("Ingrese el apellido: ")
		if nombre+" "+apellido in Agenda:
			del(Agenda[nombre+" "+apellido])
			print("\nContacto eliminado con éxito")
		else:
			print("\nDicho contacto no existe en la agenda\nERROR AL ELIMINAR CONTACTO")
	elif opcion==4:
		print("\nAdios")
	else:
		print("\nOpcion Incorrecta")