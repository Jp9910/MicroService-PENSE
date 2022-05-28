from socket import *

portaServidor = 55504

socketServidor = socket(AF_INET,SOCK_STREAM)

socketServidor.bind(('200.17.121.13',portaServidor))

socketServidor.listen(1)

while 1:
    print "O servidor esta pronto para receber"
    socketConexao, endereco = socketServidor.accept()
    nomeDoNovoArq = '/tmp/'+str(endereco[0])+'.txt'
    print 'novo arquivo sera escrito em '+nomeDoNovoArq
    arq = open(nomeDoNovoArq,'w')
    while 1:
        dados = socketConexao.recv(1024)
        if not dados:
            break
        arq.write(dados)
    arq.close()
    socketConexao.close()
    print 'Arquivo escrito. Pronto para iniciar nova conexao'