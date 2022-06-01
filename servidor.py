from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import socket
import subprocess

class Servidor(BaseHTTPRequestHandler):
    #Funcao chamada para responder uma requisicao GET de um cliente
    def do_GET(self):
        subprocessoPS = subprocess.Popen(["ps"], stdout=subprocess.PIPE)
        output, error = subprocessoPS.communicate()
        out = output.split()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Servidor HTTP - Processos Em Execucao</title></head>"))
        self.wfile.write(bytes("<p>Url requisitado: %s</p>" % self.path))
        self.wfile.write(bytes("<p>Processos rodando neste servidor: </p>"))
        self.wfile.write(bytes("<body><table>"))
        
        self.wfile.write(bytes("<thead>"))
        self.wfile.write(bytes("<tr>"))
        self.wfile.write(bytes("<th>%s</th>" %out[0]))
        self.wfile.write(bytes("<th>%s</th>" %out[1]))
        self.wfile.write(bytes("<th>%s</th>" %out[2]))
        self.wfile.write(bytes("<th>%s</th>" %out[3]))
        self.wfile.write(bytes("</tr>"))
        self.wfile.write(bytes("</thead>"))
        
        self.wfile.write(bytes("<tbody>"))
        for i in range(4, len(out), 4):
            self.wfile.write(bytes("<tr>"))
            self.wfile.write(bytes("<td>%s</td>" %out[i]))
            self.wfile.write(bytes("<td>%s</td>" %out[i+1]))
            self.wfile.write(bytes("<td>%s</td>" %out[i+2]))
            self.wfile.write(bytes("<td>%s</td>" %out[i+3]))
            self.wfile.write(bytes("</tr>"))
        #self.wfile.write(bytes("<p>Houve algum erro rodando 'ps'? %s</p>" % error))
        self.wfile.write(bytes("</tbody></table></body></html>"))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipContainer = s.getsockname()[0] #encontrar o IP do container
s.close()
print "IP do container: "+ipContainer
ipServidor = ipContainer
portaServidor = 80

if __name__ == "__main__":        
    webServer = HTTPServer((ipServidor, portaServidor), Servidor)
    print("Servidor iniciado em http://%s:%s" % (ipServidor, portaServidor)) #tambem poderia usar "0.0.0.0" em vez do ip do container

    #try:
    webServer.serve_forever()
    #except KeyboardInterrupt:
    #    pass

    webServer.server_close()
    print("Server stopped.")
