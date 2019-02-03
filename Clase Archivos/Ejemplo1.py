# -*- coding:utf-8 -*-

from io import open

direction = "/home/docente/Escritorio/ADES/archivos/ejemploArchivo.txt"

archivo_texto = open(direction, "w") # w-> abre el archivo en modo escritura (write)
frase = "Hola ADES, este es mi primer archivo\nCreado en Python"
archivo_texto.write(frase)
archivo_texto.close()

