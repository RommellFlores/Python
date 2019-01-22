class Persona():
	def __init__(self, edad, nombre, dni, correo):
		self.__edad = edad
		self.__nombre = nombre
		self.__dni = dni
		self.correo = correo

	def get_datos(self):
		return "los datos son:"+"\n"+ str(self.__edad)+ "\n" + str(self.__dni)+"\n" + str(self.__nombre)+"\n" + str(self.correo)

class Animal():
	def __init__(self, instinto):
		self.instinto = instinto
	def get_datos(self):
		return "instinto: "+ str(self.instinto)

class Estudiante(Persona, Animal):
	def __init__(self, edad, nombre, dni, correo, codigo, carrera, instinto):
		super().__init__(edad, nombre, dni, correo)
		self.__codigo = codigo
		self.carrera = carrera
		Animal.__init__(self,instinto)

	def get_datos(self):
		return super().get_datos() + str(self.__codigo) + "\n"+ str(self.carrera)+"\n"+ Animal.get_datos(self)

persona1 = Persona(14, "juanito", 123456789, "juanitosupersayayyin@uni.pe")
print(persona1.get_datos())
simple_estudiante = Estudiante(21, "cesar colorado",456123789, "cesarmaznakitukentaky@gmail.com", "7894561H", "CyCy", "ultrainstinto")
print(simple_estudiante.get_datos())