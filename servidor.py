#!/usr/bin/env python3

import socket
import socket
#import pyftpdlib
from os import listdir
from os.path import isfile, join


#servidor

def receber():
    msg = HOST_CLIENTE.recv(2048)             # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
    if (msg):
        msgdecod = msg.decode()
        return msgdecod
            
def enviar(msg):
    HOST_CLIENTE.sendall(msg.encode())


HOST_SERVIDOR = '127.0.0.1'                      # IP local
PORTA_SERVIDOR = 11500                              # Porta livre para uso
CAMINHO_PASTA = 'C://Users/PC/fr20201g04'           # Pasta com os arquivos de teste


SERVIDOR = socket.socket(                           # Cria o socket
            socket.AF_INET,                         # socket.AF_INET - Familia IPV4
            socket.SOCK_STREAM                      # socket.SOCK_STREAM - Protocolo TCP
            )
     
SERVIDOR.bind((                                     # Bind é influenciado pela familia, AF_INET pede host e porta, basicamente abre a conexao
        HOST_SERVIDOR,                              # IP 127.0.0.1 - Servidor Local
        PORTA_SERVIDOR                              # PORTA 11500 - Qualquer valor acima de 1023 é válido
    ))

SERVIDOR.listen()                                   # Libera o servidor para conexoes, algo necessario para o TCP

while True:
    SERVIDOR.listen()                                   # Libera o servidor para conexoes, algo necessario para o TCP
    HOST_CLIENTE, PORTA_CLIENTE = SERVIDOR.accept()     # Espera uma conexao com o cliente
    print('Conectado com ', PORTA_CLIENTE)
    
    protocolo = HOST_CLIENTE.recv(2048)             # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
    
    if (protocolo):
        PROTOCOLO = protocolo.decode()              # A informaçao vem em bytes, por isso precisa ser decodificada
        print('Protocolo solicitado:', PROTOCOLO)
        
        if (PROTOCOLO == "HTTP"):                       # Se o protocolo for HTTP
            request = HOST_CLIENTE.recv(2048).decode()  # Recebe os proximos parametros
            
            print("\nRequisiçao recebida.")
            file = request.split(' ')                   # Separa o caminho do arquivo do resto da requisiçao
            try:
                with open(CAMINHO_PASTA+'/html'+file[1]) as html:  # Abre o arquivo
                    text = html.read()
                    response = 'HTTP/1.1 200 OK\r\n\r\n'+text               # Monta mensagem de resposta
                    HOST_CLIENTE.sendall(response.encode())                 #Envia mensagem de resposta codificada
                    print('Resposta enviada.\n')
            except FileNotFoundError as error:                              # Verifica se houve erro na hora de abrir 
                        HOST_CLIENTE.sendall(b'404 Not Found\n')            #Envia mensagem de resposta codificada
                        print('404 Not Found:')
                        print(request)
        
        elif (PROTOCOLO == "SMTP" or PROTOCOLO == "MAIL"):  # Se o protocolo for SMTP
            request = HOST_CLIENTE.recv(2048).decode()
            user, senha = request.split(';')
            
            print("\nRequisiçao recebida.")
            
            with open(CAMINHO_PASTA+'/usuarios.txt') as file:   # Abre o arquivo de usuarios
                usuarios = file.read().split('\n')              # Separa os itens do arquivo pelas linhas
                ver = True
                for x in range(len(usuarios)):                  # For com o numero de linhas do arquivo   
                    u = usuarios[x].split(';')                  # Separa a linha do arquivo em u[0] usuario e u[1] senha
                    if (u[0]== user): 
                        ver = False# Verifica se o usuario vindo da requisiçao existe no arquivo
                        if(u[1]== senha):                       # Verifica se a senha da requisiçao eh a senha do arquivo
                            HOST_CLIENTE.sendall(b'220 localhost') 
                            msg1 = HOST_CLIENTE.recv(2048).decode()         # Inicio da 'conversa' entre servidor e cliente
                            aux, cmail = msg1.split(' ')
                            print('\n'+msg1)
                            HOST_CLIENTE.sendall(b'250 Hello '+cmail.encode()+b', pleased to meet you')                 #Envia mensagem de resposta codificada
                            msg2 = HOST_CLIENTE.recv(2048).decode()
                            print(msg2)
                            msg2r = msg2.replace(">", "")
                            msg2r = msg2r.replace("<", ";")
                            msg2r_1, email = msg2r.split(';')
                            HOST_CLIENTE.sendall(b'250 '+email.encode()+b'... Sender ok')
                            msg3 = HOST_CLIENTE.recv(2048).decode()
                            print(msg3)
                            msg3r = msg3.replace(">", "")
                            msg3r = msg3r.replace("<", ";")
                            msg3r_1, dest = msg3r.split(';')
                            HOST_CLIENTE.sendall(b'250 '+dest.encode()+b'... Recipient ok')
                            print(HOST_CLIENTE.recv(2048).decode())
                            HOST_CLIENTE.sendall(b'354 Enter mail, end with "." on a line by itself')
                            msg4 = HOST_CLIENTE.recv(2048).decode()
                            if (msg4 == '.'):
                                HOST_CLIENTE.sendall(b'250 Message accepted for delivery')
                            else:
                                with open(CAMINHO_PASTA+'/email/'+user+'.txt', 'a') as user_file: #abre o arquivo caixa de email do usuário
                                    text = ';'+msg4
                                    user_file.write(text)
                                HOST_CLIENTE.sendall(b'250 Message accepted for delivery')
                                print(HOST_CLIENTE.recv(2048).decode())
                                
                            print(HOST_CLIENTE.recv(2048).decode())
                            HOST_CLIENTE.sendall(b'221 localhost closing connection')
                            
                        else:
                            HOST_CLIENTE.sendall(b'401 Senha_incorreta\n')                      # Retorna senha incorreta pro cliente
                            print('Resposta enviada.\n')
                if (ver):    
                    HOST_CLIENTE.sendall(b'404 Usuario_nao_encontrado\n')                       # Retorna usuario nao encontrado pro cliente
                else:
                    HOST_CLIENTE.sendall(b'200 OK')       
                print('Resposta enviada.\n')
            
        elif (PROTOCOLO == "IMAP"):                         # Se o protocolo for HTTP
            request = HOST_CLIENTE.recv(2048).decode()      # Recebe os proximos parametros
            prot, user, senha = request.split(' ')          # Separa protocolo, usuario e senha vindo da requisiçao
            
            print("\nRequisiçao recebida.")
            
            with open(CAMINHO_PASTA+'/usuarios.txt') as file:   # Abre o arquivo de usuarios
                usuarios = file.read().split('\n')              # Separa os itens do arquivo pelas linhas
                
                for x in range(len(usuarios)):                  # For com o numero de linhas do arquivo   
                    u = usuarios[x].split(';')                  # Separa a linha do arquivo em u[0] usuario e u[1] senha
                    if (u[0]== user):                           # Verifica se o usuario vindo da requisiçao existe no arquivo
                        if(u[1]== senha):                       # Verifica se a senha da requisiçao eh a senha do arquivo
                            with open(CAMINHO_PASTA+'/email/'+user+'.txt') as user_file:    # Se tudo estiver certo, abre o arquivo com o nome do usaurio
                                response = user_file.read()
                                HOST_CLIENTE.sendall(response.encode())                     # retorna o conteudo do arquivo
                                print('Resposta enviada.\n')
                        else:
                            HOST_CLIENTE.sendall(b'Senha incorreta\n')                      # Retorna senha incorreta pro cliente
                            print('Resposta enviada.\n')
                    
                HOST_CLIENTE.sendall(b'Usuario nao encontrado\n')                           # Retorna usuario nao encontrado pro cliente
                print('Resposta enviada.\n')
                
        elif (PROTOCOLO == 'FTP'):
            input_usuario=receber()
            print ('usuario: '+input_usuario+'\n')
            
            with open (CAMINHO_PASTA+'/usuarios.txt') as file:
                usuarios=file.read().split('\n') #abre o arquivo de usuarios 
            
            ver = True   
            for x in range(len(usuarios)):
                u=usuarios[x].split(';') # salva usuario e sanha num array para verificar existencia
                if (u[0]== input_usuario): #se usuario encontrado
                    ver = False
                    print ("usuario encontrado, solicitando senha\n")
                    HOST_CLIENTE.sendall(b'331 Username OK, password required') #mensagem de sucesso
                    input_senha = receber () #solicita senha
                    if (u[1] == input_senha): #compara senha com salva no servidor
                        print ("senha corresponde\n")
                        rota = CAMINHO_PASTA+'/html/'
                        pasta = [f for f in listdir(rota) if isfile(join(rota, f))]
                        pasta = ' '.join(pasta)
                        enviar (pasta)      #senha corresponde; hora de enviar lista de arquivos disponíveis          
                        nomecomando = receber()
                        comando,nome=nomecomando.split(' ')
                        rota = 'C://Users/PC/fr20201g04/servidor'+'/html/' + nome
                        if (comando=='RETR'): #comando retr
                            with open(rota) as file:
                                text = file.read()
                                file.close()
                                enviar(text)
                            print ("arquivo enviado")
                        elif (comando == 'STOR'): #comando stor
                            with open(rota,"a") as file:
                                file.write(receber())
                                enviar ('arquivo gravado')
                            print ("arquivo recebido")
                    else:
                            enviar ('senha incorreta')
                            print ("senha nao corresponde\n")
            if (ver):    
                HOST_CLIENTE.sendall(b'404 Usuario_nao_encontrado\n')                       # Retorna usuario nao encontrado pro cliente
            else:
                HOST_CLIENTE.sendall(b'200 OK')
            print('Resposta enviada.\n')
                