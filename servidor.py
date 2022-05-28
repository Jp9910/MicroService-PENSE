from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from socket import *
import subprocess
class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        processos = subprocess.Popen(["ps"], stdout=subprocess.PIPE)
        output, error = processos.communicate()
        out = output.split()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>servidor http em python</title></head>"))
        self.wfile.write(bytes("<p>Url requisitado: %s</p>" % self.path))
        self.wfile.write(bytes("<p>Processos rodando neste servidor: </p>"))
        self.wfile.write(bytes("<body>"))
        self.wfile.write(bytes("<table>"))
        
        self.wfile.write(bytes("<thead>"))
        self.wfile.write(bytes("<tr>"))
        self.wfile.write(bytes("<th>%s" %out[0]))
        self.wfile.write(bytes("</th>"))
        self.wfile.write(bytes("<th>%s" %out[1]))
        self.wfile.write(bytes("</th>"))
        self.wfile.write(bytes("<th>%s" %out[2]))
        self.wfile.write(bytes("</th>"))
        self.wfile.write(bytes("<th>%s" %out[3]))
        self.wfile.write(bytes("</th>"))
        self.wfile.write(bytes("</tr>"))
        self.wfile.write(bytes("</thead>"))
        
        self.wfile.write(bytes("<tbody>"))
        for i in range(4, len(out), 4):
            self.wfile.write(bytes("<tr>"))
            self.wfile.write(bytes("<td>%s" %out[i]))
            self.wfile.write(bytes("</td>"))
            self.wfile.write(bytes("<td>%s" %out[i+1]))
            self.wfile.write(bytes("</td>"))
            self.wfile.write(bytes("<td>%s" %out[i+2]))
            self.wfile.write(bytes("</td>"))
            self.wfile.write(bytes("<td>%s" %out[i+3]))
            self.wfile.write(bytes("</td>"))
            self.wfile.write(bytes("</tr>"))
        self.wfile.write(bytes("</tbody>"))
        
        self.wfile.write(bytes("</table>"))
        #self.wfile.write(bytes("<p> Processos rodando no servidor: %s</p>" % output))
        self.wfile.write(bytes("<p>Houve algum erro rodando 'ps'? %s</p>" % error))
        self.wfile.write(bytes("</body></html>"))

portaServidor = 55504

if __name__ == "__main__":        
    webServer = HTTPServer(("localhost", portaServidor), Servidor)
    print("Server started http://%s:%s" % ("localhost", portaServidor))

    #try:
    webServer.serve_forever()
    #except KeyboardInterrupt:
    #    pass

    webServer.server_close()
    print("Server stopped.")