#!/usr/bin/env python3

import socket
import ftplib
import socket
from getpass import getpass

def receber():
    while True:
        msg = CLIENTE.recv(2048)             # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
        if (msg):
            msgdecod = msg.encode()
            return msgdecod
            
def enviar(msg):
    CLIENTE.sendall(b(msg))

CLIENTE = socket.socket(                                        # Cria o socket
        socket.AF_INET,                                         # socket.AF_INET - Familia IPV4
        socket.SOCK_STREAM                                      # socket.SOCK_STREAM - Protocolo TCP
        ) 
                                 
print('Por favor, digite o protocolo, ip destino e porta separados por espaço. (Protocolos disponiveis: HTTP, FTP, SMPT ou IMAP)')
entrada = input()                                               # Le os valores
PROTOCOLO, HOST_SERVIDOR, porta_servidor = entrada.split(' ')   # Pega os valores lidos e separa em variaveis a partir dos espaços 
PORTA_SERVIDOR = int(porta_servidor)                            # Converte o valor lido de string para int
 
CLIENTE.connect((                                               # Solicita conexao com o servidor
            HOST_SERVIDOR,                                      # IP do servidor a se conectar
            PORTA_SERVIDOR                                      # Porta a se conectar
        ))


CLIENTE.sendall(PROTOCOLO.encode())                             # Envia a mensagem codificada em bytes            

print('Conectado com ', HOST_SERVIDOR, PORTA_SERVIDOR)
    
while True:
    resposta = CLIENTE.recv(2048)                               # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
    print('Resposta: ', resposta.decode())
    break
    
    elif PROTOCOLO == 'FTP':
    print('Por favor, digite o usuario')
    usuario = input()
    enviar (usuario)
    print autorizado=receber ()
    if autorizado == b'331 Username OK, password required'
            print('\nPor favor, digite a senha\n')
            senha = getpass()
            CLIENTE.sendall(senha.encode()) 
            print autorizado=receber()
                if autorizado!='senha incorreta'
                    print 'insira o comando e o nome do arquivo separados por " " espaço:\n RETR \nSTOR\n'
                    nomecomando = input()
                    enviar (nomecomando)
                    comando,nome=nomecomando.split(' ')
                    rota = 'C:/fr202001g04/html/'+ nome
                    if comando ==   RETR                 
                        with open(rota,"a") as file:
                        file.write(receber())
                        arq.close ()
                    elif comando == STOR
                        with open(rota) as file:
                        text = file.read()
                        enviar(text)
                        receber()
    