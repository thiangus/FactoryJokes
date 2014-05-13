#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# inetclient.py - Versao 1.0
# um cliente para se conectar ao servidor multithread
# Mario O. Menezes baseado no codigo Java do 
# Prof. Elliott 

# python inetclient.py endereco_servidor numero_porta

import socket  # networking module
import sys

raw_text = "Escolha o modo do servidor! \n (piada) - (proverbio) - (manutencao) \n (quit) terminar este cliente \n (shutdown) desligar o servidor \n MODO>"

def getRemoteAddress(mode, serverName, port):
    # cria um socket Internet TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # conecta ao servidor
    print "Trying send mode> ", s
    s.connect((serverName, port))
    s.settimeout(30)
    s.send(mode)
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
        port = 1566
    else:
        serverName = args[1]  # server address
        port = int(args[2])  # server port
    
    print "Programa Inet Client entrando em execucao..."
    print "Usando o servidor: ", serverName, " Porta: ", port

    mode = ""
    while 1:
        try:
            mode = raw_input(raw_text)
            if mode.find("piada") >= 0:
                getRemoteAddress("piada", serverName, port) 
                mode = ""
            elif mode.find("proverbio") >= 0:
                getRemoteAddress("proverbio", serverName, port) 
                mode = ""
            elif mode.find("manutencao") >= 0:
                getRemoteAddress("manutencao", serverName, port) 
                mode = ""
            elif mode.find("quit") >= 0:
                print "terminando este cliente"
                break
            elif mode.find("shutdown") >= 0:
                print "solicitando encerramento do servidor ..."
                getRemoteAddress("shutdown",serverName,port)
                break
        except EnvironmentError, n:
            print "Erro: ", n
            break



if __name__ == "__main__":
    main(sys.argv)
