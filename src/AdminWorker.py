#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# AdminWorker.py - Versao 1.0

import sys
import os
import threading
from CS import CS

class AdminWorker(threading.Thread):
   
   admMode = None
   v = ''
   vlockadm = threading.Lock()
   id = 0  # proximo id de thread disponivel
  
   def __init__(self,clntsock,modeServer):
    # invoca o construtor da classe pai
    threading.Thread.__init__(self)
    # adiciona variaveis de instancia
    self.myid = AdminWorker.id
    AdminWorker.id += 1
    self.admMode = modeServer
    self.myclntsock = clntsock

   def run(self):
     try:
        print "Adm client can change mode : ", CS.adminControlSwitch
        if not CS.adminControlSwitch: 
            # Note que este trecho pode nunca ser executado
            print "Servidor em uso não pode ser acessado no momento"
            self.myclntsock.send("Servidor administrativo em uso no momento, por favor volte mais tarde!")
            raise
            # recebe um name a buscar vindo do cliente
        try:
           #command recebe piada, privervio ou manutenção para mudar seu estado
           command = self.myclntsock.recv(1024)
        except socket.error, msg:
           print "Erro no socket"
        #Nessas condicionais tem uma booleana que é setada para false para deixar ocupado o servidor deixando assim apenas um adm
	if command.find("piada") >= 0: #quando recebe piada, muda o estado para a mesma
	    self.myclntsock.send("Servidor em modo piada!")
            CS.adminControlSwitch = False
	    self.admMode.setModo(0)
	    self.myclntsock.close()
	elif command.find("proverbio") >=0: #Quando recebe proverbio, muda seu estado para o mesmo
	    self.myclntsock.send("Servidore em modo proverbio!")
            CS.adminControlSwitch = False
	    self.admMode.setModo(1)
	    self.myclntsock.close()
	elif command.find("manutencao") >=0: #Quando recebe manutenção, muda seu estado para o mesmo
	    self.myclntsock.send("Servidor em modo manutencao!")
            CS.adminControlSwitch = False
            self.admMode.setModo(2)
	    self.myclntsock.close()

     except:
       print "Unexpected error:", sys.exc_info()[0]

     if CS.controlSwitch:
       self.myclntsock.close() # fecha esta conexao, mas nao o servidor

