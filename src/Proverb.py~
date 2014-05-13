#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# Proverb.py - Versao 1.0

import sys
import os
import Pyro.core
import Pyro.naming
from Formatter import Formatter
from random import randint

class Proverb(Pyro.core.ObjBase):
   #nome do arquivo a ser aberto
   __fileName__ = "proverbios.txt"
		
   @staticmethod	
   def populateList(fileName): #Método estático que carrega um array a partir de um arquivo
    try:
     arqv = open(fileName)
     genericList = arqv.readlines() #Lê todas as linhas do arquivo e coloca em um array
     arqv.close()
    except IOError, msg:
     print msg
    return genericList
	 
   def get(self, name): #Método que traz uma proverbio aleatória a partir deste array
     genericList = Proverb.populateList(self.__fileName__) 
     index = randint(0,len(genericList)) - 1
     return Formatter.replaceByName(genericList[index],name)

#inicia proverbio deixando assim remota
Pyro.core.initServer()
ns=Pyro.naming.NameServerLocator().getNS()
daemon=Pyro.core.Daemon()
daemon.useNameServer(ns)
uri=daemon.connect(Proverb(),"proverb")
daemon.requestLoop()
