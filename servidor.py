#!/usr/bin/env python3

import socket

HOST_SERVIDOR = '127.0.0.1'                         # IP local
PORTA_SERVIDOR = 11500                              # Porta livre para uso

SERVIDOR = socket.socket(                           # Cria o socket
            socket.AF_INET,                         # socket.AF_INET - Familia IPV4
            socket.SOCK_STREAM                      # socket.SOCK_STREAM - Protocolo TCP
            )
     
SERVIDOR.bind((                                     # Bind é influenciado pela familia, AF_INET pede host e porta, basicamente abre a conexao
        HOST_SERVIDOR,                              # IP 127.0.0.1 - Servidor Local
        PORTA_SERVIDOR                              # PORTA 11500 - Qualquer valor acima de 1023 é válido
    ))

SERVIDOR.listen()                                   # Libera o servidor para conexoes, algo necessario para o TCP

HOST_CLIENTE, PORTA_CLIENTE = SERVIDOR.accept()     # Espera uma conexao com o cliente
print('Conectado com ', PORTA_CLIENTE)
    
while True:
    protocolo = HOST_CLIENTE.recv(2048)             # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
    if (protocolo):
        PROTOCOLO = protocolo.decode()              # A informaçao vem em bytes, por isso precisa ser decodificada
        print('Protocolo solicitado:', PROTOCOLO)
        HOST_CLIENTE.sendall(b'200 OK')             #Envia mensagem de resposta
    