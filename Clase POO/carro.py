class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo


class Carro(Vehiculo):
	def __init__(self, largo, ancho, marca, modelo):	
		super().__init__(marca, modelo)
		self.__largoChasis = largo
		self.anchoChasis = ancho
		self.ruedas = 4
		self.enMarcha = False

	def arranca(self):
		self.enMarcha = True

	def __estado(self):
		if(self.enMarcha):
			return "el carro esta en movimiento"
		else:
			return "el carro esta quieto"
	
	def set_largo(self, largo):
		self.__largoChasis = largo

	def get_largo(self):
		return self.__largoChasis

toyota = Carro(250, 120, "toyota", "tercel")

toyota.set_largo(300)
print (toyota.get_largo())
print (toyota.marca)
print (toyota.modelo)