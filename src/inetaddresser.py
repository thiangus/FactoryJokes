#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import traceback
import socket
import sys

def printLocalAddress():
    try:
        print "Programa INET addresser"
        me = socket.gethostbyaddr(socket.getfqdn(socket.gethostname()))
        print "Meu nome local eh:  ", me[0]
        print "Meu endereco IP eh: ", me[2][0]
    except:
        print "Parece que nao me conheco!"
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60

def printJokeOrProverbToClient(nome):
    try:
        print "Procurando ", nome, "..."
        maquina = socket.gethostbyaddr(socket.getfqdn(nome))
        print "Host name: ", maquina[0]
        print "Host IP:   ", maquina[2][0]
    except:
        print "Falha em procurar ", nome


printLocalAddress()

resposta = ""
while resposta.find("quit") < 0:
    try:
        print "\n"
        resposta = raw_input("Entre um hostname ou um endereco IP, (quit) para terminar: ")
        if resposta.find("quit") < 0:
            printJokeOrProverbToClient(resposta)
        else:
            print "terminando ..."
    except EnvironmentError, n:
            print "Erro: ", n
