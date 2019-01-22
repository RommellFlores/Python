#-*- coding: utf-8 -*-
#Manejo de excepciones

def opBásicas(num1, num2, operación):
    if operación == "suma":
        return num1 + num2
    elif operación == "resta":
        return num1 - num2
    elif operación == "multiplicación":
        return num1*num2
    elif operación == "división":
        #Manejo de la excepción al dividir por 0
        try:
            return num1/num2
        except ZeroDivisionError:
            print("Error, no se puede divir entre 0.")
    else:
        print("Error, operación incorrecta.")

operación = input("Ingrese una operación (suma, resta, multiplicación, división): ")
while True:
    try: #Manejo de excepción en el cual los tipos de datos no coinciden
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("El valor introducido no es correcto. Inténtelo de nuevo.")

resultado = opBásicas(num1, num2, operación)
if(resultado != None):
    print(resultado)

