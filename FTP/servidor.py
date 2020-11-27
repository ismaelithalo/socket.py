#!/usr/bin/env python3

import socket
import ftpdlib
from os import listdir
from os.path import isfile, join

def receber():
    while True:
        msg = HOST_CLIENTE.recv(2048)             # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
        if (msg):
            msgdecod = msg.decode()
            return msgdecod
            
def enviar(msg):
    HOST_CLIENTE.sendall(b(msg))
    
    

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
        
        elif protocolo == 'FTP':
        input_usuario=receber()
        print 'usuario: ' input_usuario '\n'
        with open ('C:/fr202001g04/usuarios.txt') as file:
        usuarios=file.read().split('\n') #abre o arquivo de usuarios 
        for x in range(len(usuarios)):
            u=usuario[x].split(';') # salva usuario e sanha num array para verificar existencia
            if u[0]== input_usuario #se usuario encontrado
                print "usuario encontrado, solicitando senha\n"
               Host_CLIENTE.sendall(b'331 Username OK, password required') #mensagem de sucesso
                input_senha = receber () #solicita senha
                if u[1] == input_senha #compara senha com salva no servidor
                    print "senha corresponde\n"
                    rota = 'C:/fr202001g04/html/'
                    enviar ([f for f in listdir(rota) if isfile(join(rota, f))])      #senha corresponde; hora de enviar lista de arquivos disponíveis          
                    nomecomando = receber()
                    comando,nome=nomecomando.split(' ')
                    rota = 'C:/fr202001g04/html/' + nome
                    if comando=='RETR' #comando retr
                        with open(rota) as file:
                        text = file.read()
                        enviar(text)
                        print "arquivo enviado"
                    elif comando == 'STOR' #comando stor
                        with open(rota,"a") as file:
                        file.write(receber())
                        enviar ('arquivo gravado')
                        print "arquivo recebido"
                else enviar ('senha incorreta')
                    print "senha nao corresponde\n"
            else Host_CLIENTE.sendall(b'usuario nao encontrado')
                print "usuario nao encontrado\n"
        
        
        
    
    