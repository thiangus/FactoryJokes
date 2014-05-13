#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# ModeServer.py - Versao 1.0

import sys
import os
import Pyro.core
import threading
import random
from CS import CS

class ModeServer():

  modeId = None #id para definir qual modo da lista será selecionado
  listMode =["joke","proverb", "maintenance"] #lista com os endereços dos modos remotos
  modelock = threading.Lock()

  def __init__(self): #Construtor que quando é chamado inicia um modo para o cliente até que o adm interfira no modo
   index = random.randint(1,len(self.listMode)) - 1 
   self.modeId = index
 
  def getModo(self): #retorna o modo apartir da lista de endereços
   return self.call(self.listMode[self.modeId])
    
  def setModo(self,modo): #seta um modo através de um id
    ModeServer.modelock.acquire()
    self.modeId = modo
    CS.adminControlSwitch = True
    ModeServer.modelock.release()

  def call(self,className): #Traz a instância através de uma chamada remota
    print "PYRONAME://"+className
    return Pyro.core.getProxyForURI("PYRONAME://"+className) 

