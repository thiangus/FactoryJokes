#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# inetclient.py - Versao 1.0
# um cliente para se conectar ao servidor multithread
# Mario O. Menezes baseado no codigo Java do 
# Prof. Elliott 

# python inetclient.py endereco_servidor numero_porta

import socket  # networking module
import sys


def getRemoteAddress(resposta, serverName, port):
    # cria um socket Internet TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # conecta ao servidor
    s.connect((serverName, port))
    s.settimeout(30)
    s.send(resposta)
    for i in range(3):
        try:
            v = s.recv(4096)
        except socket.timeout:
            print "Timeout do servidor; terminando..."
            sys.exit(-1)
        except socket.error, msg:
            print "Erro no servidor; terminando ..."
            sys.exit(-1)
        if len(v) == 0: break
        print v
    s.close()


def main(args):
    if len(args) == 1:
        serverName = "localhost"
        port = 1565
    else:
        serverName = args[1]  # server address
        port = int(args[2])  # server port
    
    print "Programa Inet Client entrando em execucao..."
    print "Usando o servidor: ", serverName, " Porta: ", port

    resposta = ""
    while 1:
        try:
            resposta = raw_input("(quit) para terminar este cliente \n(shutdown) para desligar o servidor\n_________________________\nSeu nome: ")
            if  resposta.find("quit") < 0 and resposta.find("shutdown") < 0:
                getRemoteAddress(resposta, serverName, port)
                resposta = ""
            elif resposta.find("quit") >= 0:
                print "terminando este cliente"
                break
            elif resposta.find("shutdown") >= 0:
                print "solicitando encerramento do servidor ..."
                getRemoteAddress("shutdown",serverName,port)
                break
        except EnvironmentError, n:
            print "Erro: ", n
            break



if __name__ == "__main__":
    main(sys.argv)
