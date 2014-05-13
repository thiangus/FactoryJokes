#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# Piada.py - Versao 1.0

import sys
import os
import Pyro.core
import Pyro.naming
from Formatter import Formatter
from random import randint

class Joke(Pyro.core.ObjBase):
   #nome do arquivo a ser aberto
   __fileName__ = "piadas.txt"
			
   @staticmethod	
   def populateList(fileName): #Método estático que carrega um array a partir de um arquivo
    try:
     arqv = open(fileName)
     genericList = arqv.readlines() #Lê todas as linhas do arquivo e coloca em um array
     arqv.close()
    except IOError, msg:
     print msg
    return genericList
	 
   def get(self, name): #Método que traz uma piada aleatória a partir deste array
     genericList = Joke.populateList(self.__fileName__) 
     index = randint(0,len(genericList)) - 1
     return Formatter.replaceByName(genericList[index],name)

#inicia a piada deixando assim remota
Pyro.core.initServer()
ns=Pyro.naming.NameServerLocator().getNS()
daemon=Pyro.core.Daemon()
daemon.useNameServer(ns)
uri=daemon.connect(Joke(),"joke")
daemon.requestLoop()
