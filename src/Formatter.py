import sys
import string

#Classe definida para subistituir properties por valores
class Formatter:
	
	@staticmethod
	def replaceByName(line, name): #subistitui a key property.name pelo nome do cliente
	 return line.replace("property.name",name)
