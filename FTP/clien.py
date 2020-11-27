import socket
from ftplib import ftplib
from getpass import getpass

#client 


def receber():
    while True:
        msg = CLIENTE.recv(2048)             # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
        if (msg):
            msgdecod = msg.encode()
            return msgdecod
            
def enviar(msg):
    CLIENTE.sendall(b(msg))
    

    
    


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
