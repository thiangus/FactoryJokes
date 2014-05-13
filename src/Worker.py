#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# Worker.py - Versao 1.0

import socket  # networking module
import sys
import threading
from CS import CS

class Worker(threading.Thread):

    # v e vlock sao variaveis de classe
   v = ''
   vlock = threading.Lock()
   id = 0  # proximo id de thread disponivel
   MODE = None
   
   def __init__(self,clntsock,modeServer):
      # invoca o construtor da classe pai
      threading.Thread.__init__(self)
      # adiciona variaveis de instancia
      self.myid = Worker.id
      Worker.id += 1
      self.myclntsock = clntsock
      self.MODE = modeServer
      
   def printJokeOrProverbToClient(self,name):
    try:
     self.myclntsock.send(name)
    except:
        self.myclntsock.send("Falha em procurar %s" % (name))
        print "Falha em procurar ", name

   def run(self):
      try:
         if not CS.controlSwitch: 
             # Note que este trecho pode nunca ser executado
             print "Servidor esta agora desligando"
             self.myclntsock.send("Servidor esta agora desligando. Goodbye!")
             raise
         # recebe um name a buscar vindo do cliente
         try:
            name = self.myclntsock.recv(1024)
         except socket.error, msg:
             print "Erro no socket"

         if name.find("shutdown") >= 0: 
             print "Servidor esta agora desligando a pedido do cliente"
             self.myclntsock.send("Servidor esta agora desligando. Goodbye!")
             Worker.vlock.acquire()
             CS.controlSwitch = False
             Worker.vlock.release()
             self.myclntsock.close()
         elif len(name) > 0:
             try: 
                 self.myclntsock.send("Procurando " + name)
                 if(self.MODE != None):
                  self.printJokeOrProverbToClient(self.MODE.getModo().get(str(name)))
             except socket.error, msg:
                 print "Erro no socket, terminando ..."
      except:
         print "Unexpected error:", sys.exc_info()[0]

      if CS.controlSwitch:
        self.myclntsock.close() # fecha esta conexao, mas nao o servidors
