# -*- coding: utf-8 -*-

from io import open
import os.path

direction = "/home/docente/Escritorio/ADES/archivos/ejemploArchivo2.txt"

def Revisión(archivo):
	return os.path.exists(archivo)

if Revisión(direction):
	#si en lugar de "r", colocamos "r+", el archivo se abre en modo lectura/escritura
	with open(direction, "r+") as file:
		texto = file.read()
		file.seek(0)
		lines = file.readlines()
		print(texto)
		print()
		print(lines)
		print(lines[0])
		lines[0] = "Hola ADES, agregué esta línea desde afuera\n" 
		file.seek(0)
		file.writelines(lines)
else:
	with open(direction, "w", encoding="utf-8") as file:
		frase = "Hola ADES\nEste es mi segundo archivo\nCreado con Python"
		file.write(frase)

