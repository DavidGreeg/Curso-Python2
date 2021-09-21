

import random


#Clase
class mamifero():
	vertebrado = True
	pelo = True

	#Atriburos de instancia
	alimentacion = ''
	tamanho = None
	peso = None 
	progenie = 0

	#Cuantos puede tener y cuantos van a sobrevivir
	def reproducirse (self, max_progenie):
		progen = random.choice(range(max_progenie))
		#print(progen,type(progen))
		self.progenie += progen

	def crecer(self, crecimiento):
		self.altura += crecimiento
		self.peso += crecimiento*0.4

#Crear clase 'berd' con atributos 'nombre' y 'edad'. Que tenga método 'salute' que imprima 'hey tommy'
class berd():
	nombre = ''
	edad = None

	def salute(self, saludo = 'hey tommy'):
		print('hey tommmy') 


if __name__ == "__main__":
	perro = mamifero()
	perro.vertebrado

	#Probamos nuestros métodos
	perro.alimentacion = 'omnivoro'
	perro.altura = 43
	perro.peso = 6.1
	
	#Antes de metodo reproducirse()
	print(perro.progenie)
	#Después del método reproducirse
	perro.reproducirse(6)
	print(perro.progenie)

	phillip = berd()
	phillip.salute()
