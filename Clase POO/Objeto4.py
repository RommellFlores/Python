# -*- coding: utf-8 -*-
#Herencia
class vehículo():
    #Constructor
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__arrancar = False
        self.__acelera = False
        self.__frena = False
    #Métodos
    def arrancar(self):
        self.__arrancar = True

    def acelera(self):
        self.__acelera = True

    def frena(self):
        self.__frena = True

    def estado(self):
        print(f"La marca es: {self.__marca}\nEl modelo es: {self.__modelo}")
        print(f"Arrancar: {self.__arrancar}\nAcelera: {self.__acelera}")
        print(f"Frena: {self.__frena}")

#La clase moto hereda de Vehículo
class moto(vehículo):
    #Atributo
    __haciendoKballito = ""
    #Métodos
    def kballito(self):
        self.__haciendoKballito = "Estoy haciendo kballito"
    #Método sobreescrito
    def estado(self):
        #Llamamos al método de la clase padre
        super().estado()
        print(self.__haciendoKballito)

class vehículoEléctrico():
    #Constructor
    def __init__(self):
        self.__energía = 0
        self.__cargado = False
    #Métodos
    def cargar(self):
        self.__cargado = True
        while True:
            try:
                self.__energía = float(input("Ingrese el porcentaje de carga: "))
                if self.__energía <= 0:
                    raise ValueError
                if self.__energía > 100:
                    raise ValueError
                else:
                    break
            except ValueError:
                if self.__energía < 0:
                    print("El porcentaje no puede ser negativo.")    
                elif self.__energía == 0:
                    print("El porcentaje no puede ser 0.")
                elif self.__energía > 100:
                    print("No existe un porcentaje mayor a 100%")
                else:    
                    print("Parámetro equivocado. Intente nuevamente.")
            self.__energía = 0

    def estado(self):
        if self.__cargado:
            print(f"El vehículo está cargado, y su porcentaje de carga es: {self.__energía}%.")
        else:
            print("El vehículo no está cargado")
            
#Herencia múltiple
class bicicleta(vehículoEléctrico,vehículo):
    def __init__(self, marca, modelo):
        vehículo.__init__(self,marca,modelo)
        super().__init__()
    def estado(self):
        vehículo.estado(self)
        super().estado()

miMoto = moto("Harley Davidson", "FXDR")
miMoto.kballito()
miMoto.estado()

print("\nSegunda instancia\n")

mibici = vehículoEléctrico()
mibici.cargar()
mibici.estado()

print("\nTercer instancia - Herencia múltiple\n")

mibici2 = bicicleta("Specialized", "Venge")
mibici2.estado()

