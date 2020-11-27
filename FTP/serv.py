import socket
import pyftpdlib
from os import listdir
from os.path import isfile, join


#servidor

def receber():
    while True:
        msg = HOST_CLIENTE.recv(2048)             # Recv ou receive, recebe o dado vindo da conexao com o cliente, 2048 é o buffer recomendado
        if (msg):
            msgdecod = msg.decode()
            return msgdecod
            
def enviar(msg):
    HOST_CLIENTE.sendall(b(msg))


	

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
