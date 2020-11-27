#!/usr/bin/env python3

import socket

#client 

CAMINHO_PASTA = 'C://Users/PC/fr20201g04'           # Pasta com os arquivos de teste

CLIENTE = socket.socket(                                                # Cria o socket
        socket.AF_INET,                                                 # socket.AF_INET - Familia IPV4
        socket.SOCK_STREAM                                              # socket.SOCK_STREAM - Protocolo TCP
        ) 

def receber():
        msg = CLIENTE.recv(2048)             # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
        if (msg):
                msgdecod = msg.decode()
                return msgdecod
            
def enviar(msg):
    CLIENTE.sendall(msg.encode())

                                 
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
                
                elif (PROTOCOLO == "MAIL" or PROTOCOLO == "SMTP"):                      #Protocolo email
                        CLIENTE.sendall(PROTOCOLO.encode())
                        print('\nDigite MAIL <usuario> <senha> <from> <to> <subject> <texto>.')
                        mail = input()
                        prot, user, senha, remet, dest, assun, texto = mail.split(' ')          #separa os inputs em variáveis para facilitar a comunicação
                        request = user+';'+senha
                        CLIENTE.sendall(request.encode())
                        response = CLIENTE.recv(2048).decode()
                        print(response)
                        response_code, resto = response.split(' ')
                        if (response_code == 401 or response_code == 404):                      #verifica se não houve resposta de erro
                                break
                        aux, cmail = remet.split('@')
                        CLIENTE.sendall(b'HELO '+cmail.encode())                                #inicio da comunicação smtp
                        print(CLIENTE.recv(2048).decode())
                        CLIENTE.sendall(b'MAIL FROM: <'+remet.encode()+b'>')
                        print(CLIENTE.recv(2048).decode())
                        CLIENTE.sendall(b'RCPT TO: <'+dest.encode()+b'>')
                        print(CLIENTE.recv(2048).decode())
                        CLIENTE.sendall(b'DATA')
                        print(CLIENTE.recv(2048).decode())
                        CLIENTE.sendall(texto.encode())
                        CLIENTE.sendall(b'.')
                        print(CLIENTE.recv(2048).decode())
                        CLIENTE.sendall(b'QUIT')
                        print(CLIENTE.recv(2048).decode())
                
                elif (PROTOCOLO == 'FTP'):
                        CLIENTE.sendall(PROTOCOLO.encode())
                        print('Por favor, digite o usuario')
                        usuario = input()
                        enviar (usuario)
                        autorizado=receber()
                        print(autorizado)
                        if (autorizado == '331 Username OK, password required'):
                                print('\nPor favor, digite a senha\n')
                                senha = input()
                                CLIENTE.sendall(senha.encode()) 
                                autorizado=receber()
                                print(autorizado)
                                if (autorizado!='senha incorreta'):
                                        print ('\ninsira o comando (RETR / STOR) e o nome do arquivo separados por " " espaço:')
                                        print ('Ex. RETR teste.html\n')
                                        nomecomando = input()
                                        enviar (nomecomando)
                                        comando,nome=nomecomando.split(' ')
                                        rota = CAMINHO_PASTA+'/html/'+ nome
                                        if (comando ==  'RETR'):                 
                                                with open(rota,"a") as file:
                                                        file.write(receber())
                                                        break;
                                        elif (comando == 'STOR'):
                                                with open(rota) as file:
                                                        text = file.read()
                                                        enviar(text)
                                                print(receber())
                                else:
                                        break;
                        else:
                                break;
                resposta = CLIENTE.recv(2048)                                   # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
                print('Resposta: \n{}'.format(resposta.decode()))
                break
                               
CLIENTE.close()                                  # Finaliza a conexao
                
    