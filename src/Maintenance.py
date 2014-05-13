#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# Maintenance.py - Versao 1.0

import sys
import os
import Pyro.core
import Pyro.naming

class Maintenance(Pyro.core.ObjBase):

  def get(self, name): #Traz a mensagem de manutenção junto com o nome do cliente
   return name + " desculpe no momento estamos em manutencao!!"

#inicia manutenção deixando assim remota
Pyro.core.initServer()
ns=Pyro.naming.NameServerLocator().getNS()
daemon=Pyro.core.Daemon()
daemon.useNameServer(ns)
uri=daemon.connect(Maintenance(),"maintenance")
daemon.requestLoop()
  
  
