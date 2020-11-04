#!/usr/bin/env python3

import socket

CLIENTE = socket.socket(                                                # Cria o socket
        socket.AF_INET,                                                 # socket.AF_INET - Familia IPV4
        socket.SOCK_STREAM                                              # socket.SOCK_STREAM - Protocolo TCP
        ) 
                                 
while True:
        print('Por favor, digite o protocolo, ip destino e porta separados por espaço, ou "FECHAR" para encerrar a comunicação.')
        print('(Protocolos disponiveis: HTTP, FTP, SMPT ou IMAP)')
        entrada = input()                                                       # Le os valores
        if (entrada):
                if (entrada == 'FECHAR' or entrada == 'fechar' or entrada == 'Fechar'):
                        break
                
                PROTOCOLO, HOST_SERVIDOR, porta_servidor = entrada.split(' ')   # Pega os valores lidos e separa em variaveis a partir dos espaços 
                PORTA_SERVIDOR = int(porta_servidor)                            # Converte o valor lido de string para int

                CLIENTE.connect((                                               # Solicita conexao com o servidor
                HOST_SERVIDOR,                                                  # IP do servidor a se conectar
                PORTA_SERVIDOR                                                  # Porta a se conectar
                ))
                
                print('Conectado com ', HOST_SERVIDOR, PORTA_SERVIDOR)

                if(PROTOCOLO == "HTTP"):
                        CLIENTE.sendall(PROTOCOLO.encode())                             # Envia a mensagem codificada em bytes
                        print('\nDigite o método HTTP, seguido por <rota+arquivo> e a versão do HTTP.')
                        print('(Ex. GET /index.html HTTP/1.1)')
                        http = input()
                        request = http+'\r\nHost: localhost\r\n\r\n'
                        
                        CLIENTE.sendall(request.encode())                               # Envia a mensagem codificada em bytes            
                
                elif (PROTOCOLO == "IMAP"):
                        CLIENTE.sendall(PROTOCOLO.encode())
                        print('\nDigite IMAP <usuario> <senha>')
                        imap = input()
                        CLIENTE.sendall(imap.encode())
                
                elif (PROTOCOLO == "MAIL" or PROTOCOLO == "SMTP"):
                        print('\nDigite MAIL <usuario> <senha> <from> <to> <subject> <texto>.')
                        mail = input()
                        prot, user, senha, remet, dest, assun, texto = mail.split(' ')
                        CLIENTE.sendall(imap.encode())
                        
                resposta = CLIENTE.recv(2048)                                   # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
                print('Resposta: \n{}'.format(resposta.decode()))
                break
                               
CLIENTE.close()                                                                 # Finaliza a conexao
                
    