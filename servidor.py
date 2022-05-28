from http.server import BaseHTTPRequestHandler, HTTPServer
from socket import *

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

portaServidor = 55504

socketServidor = socket(AF_INET,SOCK_STREAM)
ipservidorufs = '200.17.121.13'
socketServidor.bind(('',portaServidor))
socketServidor.listen(1)

if __name__ == "__main__":        
    webServer = HTTPServer(('localhost', portaServidor), Servidor)
    print("Server started http://%s:%s" % ('localhost', portaServidor))

    #try:
    webServer.serve_forever()
    #except KeyboardInterrupt:
    #    pass

    webServer.server_close()
    print("Server stopped.")

# while 1:
#     print "O servidor esta pronto para receber"
#     socketConexao, endereco = socketServidor.accept()
#     nomeDoNovoArq = '/tmp/'+str(endereco[0])+'.txt'
#     print 'novo arquivo sera escrito em '+nomeDoNovoArq
#     arq = open(nomeDoNovoArq,'w')
#     while 1:
#         dados = socketConexao.recv(1024)
#         if not dados:
#             break
#         arq.write(dados)
#     arq.close()
#     socketConexao.close()
#     print 'Arquivo escrito. Pronto para iniciar nova conexao'