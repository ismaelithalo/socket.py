#!/usr/bin/env python3

import socket



CLIENTE = socket.socket(
        socket.AF_INET,                         # socket.AF_INET - Familia IPV4
        socket.SOCK_STREAM                      # socket.SOCK_STREAM - Protocolo FTP
        ) 
                                 
print('Por favor, digite o protocolo, ip destino e porta separados por espaço. (Protocolos disponiveis: HTTP, FTP, SMPT ou IMAP)')
entrada = input()
PROTOCOLO, HOST_SERVIDOR, porta_servidor = entrada.split(' ')
PORTA_SERVIDOR = int(porta_servidor)            # Converte o valor lido de string para int
 
CLIENTE.connect((
            HOST_SERVIDOR, 
            PORTA_SERVIDOR
        ))

# Envia a mensagem codificada em bytes
CLIENTE.sendall(PROTOCOLO.encode())             

print('Conectado com ', HOST_SERVIDOR, PORTA_SERVIDOR)
    
while True:
    # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
    resposta = CLIENTE.recv(2048)
    print('Resposta: ', resposta.decode())
    break
    