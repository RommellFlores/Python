# -*- coding: utf-8 -*-

class MiError(Exception):
    def __init__(self):
        print("Este es nuestro error")
        
try:
    n = int(input("Ingrese un número: "))
    if n < 0:
        raise MiError
except MiError:
    print("Hola")
