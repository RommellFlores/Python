# -*- coding: utf-8 -*-

#Manejo de Excepciones
import math

#Función que calcula una raíz
def calculaRaíz(número):
    if número < 0:
        raise ValueError ("El número no puede ser negativo")
    else:
        return math.sqrt(número)

#Manejo de error de introducción de parámetros no válidos
while True:
    try:
        NúmeroXoperar = float(input("Introduce un número: "))
        break
    except ValueError:
        print("Valor ingresado no válido. Inténtelo nuevamente.")

#Manejo de error cuando se ingresa un número negativo
try:
    print(f"La raíz de {NúmeroXoperar} es {calculaRaíz(NúmeroXoperar):.5f}.")
except ValueError as ErrorNúmeroNegativo:
    print(ErrorNúmeroNegativo)
    
#Finalización de programa
print("Programa finalizado")

