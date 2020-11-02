#!/usr/bin/env python3

import socket

CLIENTE = socket.socket(
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
    