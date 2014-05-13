#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# inetserverselect-esqueleto.py - Versao 1.0
# um servidor multithread asincrono que escuta em 
# duas portas: uma normal e outra para administracao
# Mario O. Menezes 


import socket  # networking module
import sys
import threading
import select
import signal
import random
from Worker import Worker
from ModeServer import ModeServer
from AdminWorker import AdminWorker
    
class MainServer(object):
    # classe principal que cria os sockets. atraves do modulo select, verifica qual socket esta pronto para
    # ser atendido e atende-o, passando para uma thread (normal ou admin).
    """ Simple server listening on 2 ports, using select """
    MyModeServer = None
    mythreads = None
    myadmthreads = None
    outputs = None
    
    def __init__(self, port=1565 ,admport=1566, backlog=5):
        self.clients = 0
        # Client threads
        self.mythreads = []
        self.myadmthreads = []
        self.MyModeServer = ModeServer()
        #Output socket list
        self.outputs = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('',port))
        print 'Escutando na porta ',port,'...piadas, proverbios e manutenção!'
        self.server.listen(backlog)
        # administrative client connects to port 1566
        self.admserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.admserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.admserver.bind(('',admport))
        print 'Listening to Adm port',admport,'...administrative client!'
        self.admserver.listen(backlog)

        # Trap keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)
        
    def sighandler(self, signum, frame):
        # Close the server
        print 'Shutting down server...'
        # Close existing client sockets
        for o in self.outputs:
            o.close()
            
        self.server.close()
        self.admserver.close()

        
    def serve(self):
        
        inputs = [self.server,self.admserver,sys.stdin]
        self.outputs = []

        running = 1

        while running:

            try:
                inputready,outputready,exceptready = select.select(inputs, self.outputs, [])
            except select.error, e:
                break
            except socket.error, e:
                break

            for s in inputready:

                if s == self.server:
                    # handle the server socket
                    client, address = self.server.accept()
                    print 'Cliente: conexao  %d vinda de  %s' % (client.fileno(), address)
                    s = Worker(client,self.MyModeServer)
                    self.mythreads.append(s)
                    s.start()
                    
                elif s == self.admserver:
                    # handle the admin server socket
                    admclient, admaddress = self.admserver.accept()
                    print 'Admserver: got adm connection %d from %s' % (admclient.fileno(), admaddress)
                    adminW = AdminWorker(admclient,self.MyModeServer)
                    self.myadmthreads.append(adminW)
                    adminW.start()
                else:
                    # handle all other sockets
                    try:
                        # data = s.recv(BUFSIZ)
                        data = s.read(1024)
                        if data:
                            print "....nao sei porque executou isto!"
                            print " ...soh o ADM manda mensagem para o servidor!"
                        else:
                            print ' piadaserver: %d hung up' % s.fileno()
                            self.clients -= 1
                            s.close()
                            inputs.remove(s)
                            self.outputs.remove(s)
                                
                    except socket.error, e:
                        # Remove
                        inputs.remove(s)
                        self.outputs.remove(s)
                        
        # espera todas as threads clientes terminarem
        for t in self.mythreads:
            t.join()
        self.server.close()
        # espera todas as threads adm terminarem; só poderia ter uma, mas ...
        for t in self.myadmthreads:
            t.join()
        self.admserver.close()

if __name__ == "__main__":
    MainServer().serve()

